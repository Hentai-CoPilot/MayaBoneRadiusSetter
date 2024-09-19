import maya.cmds as cmds

def set_radius_for_hierarchy(joint, radius_value=1):
    # 現在のボーンにradiusを適用
    cmds.setAttr(f"{joint}.radius", radius_value)
    
    # 子ボーンを取得
    children = cmds.listRelatives(joint, children=True, type='joint')
    
    if children:
        for child in children:
            # 子ボーンに対して再帰的に処理を行う
            set_radius_for_hierarchy(child, radius_value)

# 選択したボーン（親ボーン）を取得
selected_objects = cmds.ls(selection=True, type='joint')

# ボーンが選択されているか確認
if selected_objects:
    for joint in selected_objects:
        # 親ボーンとその階層のすべてのボーンにradiusを適用
        set_radius_for_hierarchy(joint, radius_value=0.1)
else:
    cmds.warning("ボーンが選択されていません。親ボーンを選択してください。")
