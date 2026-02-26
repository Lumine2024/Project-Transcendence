import converter
import ftb_snbt_lib as slib

c1g = converter.Graph("Chapter 3", 2)
c1g.add_node(converter.Node("glog", "Get Logs", "If you want to get rich please get logs", [
    converter.ItemType("minecraft:oak_log", 1)
], [
    converter.ItemType("minecraft:oak_log", 64)
]))
c1g.add_node(converter.Node("gstone", "Get Cobblestones", "", [
    converter.ItemType("minecraft:cobblestone", 20)
], [
    converter.ItemType("minecraft:cobblestone", 64)
]))
c1g.add_edge("glog", "gstone")
compound = converter.convert(c1g)
s = slib.dumps(compound)
with open("chapter_3.snbt", "w", encoding="utf-8") as f:
    f.write(s)