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

# 選択されたジョイントをフルパス名で取得
selected_objects = cmds.ls(selection=True, type='joint', long=True)

# ジョイントが選択されているか確認
if selected_objects:
    for joint in selected_objects:
        # 親ジョイントとその階層に半径を適用
        set_radius_for_hierarchy(joint, radius_value=0.1)
else:
    cmds.warning("ジョイントが選択されていません。親ジョイントを選択してください。")
