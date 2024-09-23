import maya.cmds as cmds

def set_radius_for_hierarchy(joint, radius_value=1.0):
    # フルパス名を使用して、正しいオブジェクトを操作していることを確認
    joint_full_path = cmds.ls(joint, long=True)[0]
    
    # ジョイントに半径属性があるか確認
    if cmds.attributeQuery('radius', node=joint_full_path, exists=True):
        # 現在のジョイントに半径を適用
        cmds.setAttr(f"{joint_full_path}.radius", radius_value)
    else:
        cmds.warning(f"'{joint_full_path}'には半径属性がありません。")
    
    # 子ジョイントをフルパス名で取得
    children = cmds.listRelatives(joint_full_path, children=True, type='joint', fullPath=True)
    
    if children:
        for child in children:
            # 再帰的に子ジョイントに半径を適用
            set_radius_for_hierarchy(child, radius_value)

def apply_radius(*args):
    # スライダーの値を取得
    radius_value = cmds.floatSliderGrp(slider, query=True, value=True)
    
    # 選択されたジョイントをフルパス名で取得
    selected_objects = cmds.ls(selection=True, type='joint', long=True)
    
    # ジョイントが選択されているか確認
    if selected_objects:
        for joint in selected_objects:
            # 親ジョイントとその階層に半径を適用
            set_radius_for_hierarchy(joint, radius_value)
    else:
        cmds.warning("ジョイントが選択されていません。親ジョイントを選択してください。")

# ウィンドウが存在する場合は削除
if cmds.window("radiusWindow", exists=True):
    cmds.deleteUI("radiusWindow", window=True)

# ウィンドウの作成
window = cmds.window("radiusWindow", title="Set Joint Radius", widthHeight=(300, 100))

# レイアウト
cmds.columnLayout(adjustableColumn=True)

# スライダーの作成 (最大値10、ステップ0.1) - 値が変更されたらapply_radiusを呼び出す
slider = cmds.floatSliderGrp(field=True, minValue=0.01, maxValue=10, value=1.0, step=0.01, dragCommand=apply_radius)

# Applyボタンの作成
cmds.button(label="Apply", command=apply_radius)

# ウィンドウの表示
cmds.showWindow(window)
