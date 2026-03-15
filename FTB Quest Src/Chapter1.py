import converter as c
import ftb_snbt_lib as slib

c1g = c.Graph("第一章：机械与资源", 0)
c1g.add_node(c.Node("get logs", "获取木头", "古人云：要致富先撸树。获取一个木头吧！", [
    c.ItemType("minecraft:oak_log", 10)
], [
    c.ItemType("minecraft:oak_log", 64)
]))
c1g.add_node(c.Node("get stones", "获取石头", "木镐只有3点耐久，赶快用掉吧！", [
    c.ItemType("minecraft:cobblestone", 3)
], [
    c.ItemType("minecraft:stone_axe", 1),
    c.ItemType("minecraft:stone_pickaxe", 1),
    c.ItemType("minecraft:stone_shovel", 1)
]))
c1g.add_edge("get logs", "get stones")
c1g.add_node(c.Node("get irons", "获取铁锭", "我 有 20 铁 你 怕 不 怕", [
    c.ItemType("minecraft:iron_ingot", 20)
], [
    c.ItemType("minecraft:iron_pickaxe", 1),
    c.ItemType("minecraft:iron_helmet", 1),
    c.ItemType("minecraft:iron_chestplate", 1),
    c.ItemType("minecraft:iron_leggings", 1),
    c.ItemType("minecraft:iron_boots", 1)
]))
c1g.add_edge("get stones", "get irons")
c1g.add_node(c.Node("get coppers", "获取铜锭", "", [
    c.ItemType("minecraft:copper_ingot", 20)
], [
    c.ItemType("minecraft:iron_pickaxe", 1)
]))
c1g.add_edge("get stones", "get coppers")
c1g.add_node(c.Node("get zincs", "获取锌锭", "", [
    c.ItemType("create:zinc_ingot", 20)
], [
    c.ItemType("create:zinc_ingot", 64)
]))
c1g.add_edge("get irons", "get zincs")
c1g.add_node(c.Node("get kelps", "获取海带", "推荐在海上建家的一万个理由", [
    c.ItemType("minecraft:kelp", 32)
], [
    c.ItemType("minecraft:kelp", 128)
]))
c1g.add_edge("get logs", "get kelps")
c1g.add_node(c.Node("get slimeballs", "获取粘液球", "如果找不到沼泽，那就试着种小麦吧", [
    c.ItemType("minecraft:slime_ball", 2)
], [
    c.ItemType("minecraft:slime_ball", 64)
]))
c1g.add_node(c.Node("get redstones", "获取红石", "原版很牛，在机械动力里也很牛", [
    c.ItemType("minecraft:redstone", 20)
], [
    c.ItemType("minecraft:redstone", 64)
]))
c1g.add_edge("get irons", "get redstones")
c1g.add_node(c.Node("get diamonds", "获取钻石", "哪个玩MC的会不喜欢钻石呢", [
    c.ItemType("minecraft:diamond", 1)
], [
    c.ItemType("minecraft:diamond_axe", 1),
    c.ItemType("minecraft:diamond_pickaxe", 1),
    c.ItemType("minecraft:diamond_sword", 1),
    c.ItemType("minecraft:diamond_shovel", 1),
    c.ItemType("minecraft:diamond_hoe", 1),
    c.ItemType("minecraft:diamond_helmet", 1),
    c.ItemType("minecraft:diamond_chestplate", 1),
    c.ItemType("minecraft:diamond_leggings", 1),
    c.ItemType("minecraft:diamond_boots", 1)
]))
c1g.add_edge("get irons", "get diamonds")
c1g.add_node(c.Node("go to nether", "前往下界", "知道你要回家，穿点衣服别伤着了", [
    c.AdvancementType("story/enter_the_nether")
], [
    c.ItemType("minecraft:golden_helmet", 1)
]))
c1g.add_edge("get irons", "go to nether")
potion = {}
potion["Potion"] = slib.String("minecraft:fire_resistance")
c1g.add_node(c.Node("get blaze rod", "获得烈焰棒", "和邻居进行友好交谈", [
    c.ItemType("minecraft:blaze_rod", 1)
], [
    c.ItemType("minecraft:potion", 1, slib.Compound(potion))
]))
c1g.add_edge("go to nether", "get blaze rod")
c1g.add_node(c.Node("find bastion", "进入猪灵堡垒", "到 家 了", [
    c.AdvancementType("nether/find_bastion")
], [
    c.ItemType("minecraft:gold_ingot", 40)
]))
c1g.add_edge("go to nether", "find bastion")
c1g.add_node(c.Node("distract piglin", "紧张刺激的交易", "金块是大家的，金锭是自己的", [
    c.AdvancementType("nether/distract_piglin")
], [
    c.ItemType("minecraft:gold_ingot", 24)
]))
c1g.add_edge("go to nether", "distract piglin")
c1g.add_node(c.Node("enter the end", "前往末地", "猜末影龙死法", [
    c.AdvancementType("story/enter_the_end")
], [
    c.ItemType("minecraft:white_bed", 8),
    c.ItemType("minecraft:bow", 1),
    c.ItemType("minecraft:arrow", 64)
]))
c1g.add_edge("get blaze rod", "enter the end")
c1g.add_node(c.Node("the end", "干掉末影龙", "今天是什么材质的防伪标识呢", [
    c.AdvancementType("end/kill_dragon")
], [
    c.ItemType("minecraft:elytra", 1)
]))
c1g.add_node(c.Node("get andesite", "获取安山岩", "老大老大，你说，加入机械动力模组后，我就不再是三废石了吗", [
    c.ItemType("minecraft:andesite", 10)
], [
    c.ItemType("minecraft:andesite", 64)
]))
c1g.add_edge("get stones", "get andesite")
c1g.add_node(c.Node("get andesite alloy", "合成安山合金", "", [
    c.ItemType("create:andesite_alloy", 1)
], [
    c.ItemType("create:andesite_alloy", 64)
]))
c1g.add_edge("get andesite", "get andesite alloy")
c1g.add_edge("get irons", "get andesite alloy")
c1g.add_edge("enter the end", "the end")
c1g.add_node(c.Node("water wheel", "水车——你的第一个应力源", "河 动 力", [
    c.ItemType("create:water_wheel", 1)
], [
    c.ItemType("create:large_water_wheel", 1)
]))
c1g.add_edge("get andesite alloy", "water wheel")
c1g.add_node(c.Node("windmill", "风车", "该养羊了", [
    c.ItemType("create:windmill_bearing", 1)
], [
    c.ItemType("minecraft:wool", 64)
]))
c1g.add_edge("get andesite alloy", "windmill")

c1g.add_node(c.Node("mechanical press", "动力冲压机", "铁板！铜板！金板！黄铜板！", [
    c.ItemType("create:mechanical_press", 1)
], [
    c.ItemType("minecraft:iron_ingot", 16)
]))
c1g.add_edge("get andesite alloy", "mechanical press")
c1g.add_edge("get irons", "mechanical press")

c1g.add_node(c.Node("belt", "传送带", "", [
    c.ItemType("create:belt_connector", 8)
], [
    c.ItemType("create:andesite_alloy", 32)
]))
c1g.add_edge("get kelps", "belt")
c1g.add_edge("get andesite alloy", "belt")

c1g.add_node(c.Node("gearbox", "十字齿轮箱", "拒绝做齿轮仙人，从你他做起", [
    c.ItemType("create:gearbox", 1)
], [
    c.ItemType("minecraft:copper_ingot", 24)
]))
c1g.add_edge("get andesite alloy", "gearbox")

c1g.add_node(c.Node("mechanical bearing", "动力轴承", "", [
    c.ItemType("create:mechanical_bearing", 1)
], [
    c.ItemType("create:zinc_ingot", 16)
]))
c1g.add_edge("get andesite alloy", "mechanical bearing")

c1g.add_node(c.Node("mechanical mixer", "动力搅拌器", "搅啊搅啊搅朋友", [
    c.ItemType("create:mechanical_mixer", 1)
], [
    c.ItemType("create:andesite_alloy", 32)
]))
c1g.add_edge("mechanical press", "mechanical mixer")
c1g.add_edge("get coppers", "mechanical mixer")

c1g.add_node(c.Node("fluid tank", "流体储罐", "", [
    c.ItemType("create:fluid_tank", 1)
], [
    c.ItemType("create:fluid_tank", 8)
]))
c1g.add_edge("get coppers", "fluid tank")
c1g.add_edge("get andesite alloy", "fluid tank")

c1g.add_node(c.Node("blaze burner", "烈焰人燃烧室", "燃起来了！", [
    c.ItemType("create:blaze_burner", 1)
], [
    c.ItemType("create:blaze_burner", 4)
]))
c1g.add_edge("get blaze rod", "blaze burner")
c1g.add_edge("mechanical press", "blaze burner")

c1g.add_node(c.Node("get brass", "合成黄铜锭", "？！黄铜！？", [
    c.ItemType("create:brass_ingot", 16)
], [
    c.ItemType("create:brass_ingot", 64)
]))
c1g.add_edge("get coppers", "get brass")
c1g.add_edge("get zincs", "get brass")
c1g.add_edge("blaze burner", "get brass")
c1g.add_edge("mechanical mixer", "get brass")

c1g.add_node(c.Node("mechanical crafter", "动力合成器", "合 成 大 配 方", [
    c.ItemType("create:mechanical_crafter", 3)
], [
    c.ItemType("create:mechanical_crafter", 18)
]))
c1g.add_edge("get brass", "mechanical crafter")

c1g.add_node(c.Node("deployer", "机械手", "神之手这一块", [
    c.ItemType("create:deployer", 1)
], [
    c.ItemType("create:deployer", 1)
]))
c1g.add_edge("get brass", "deployer")

c1g.add_node(c.Node("precision mechanism", "精密构件", "", [
    c.ItemType("create:precision_mechanism", 1)
], [
    c.ItemType("create:precision_mechanism", 5)
]))
c1g.add_edge("deployer", "precision mechanism")

c1g.add_node(c.Node("rotation speed controller", "转速控制器", "", [
    c.ItemType("create:rotation_speed_controller", 1)
], [
    c.ItemType("create:rotation_speed_controller", 2)
]))
c1g.add_edge("precision mechanism", "rotation speed controller")

c1g.add_node(c.Node("encased fan", "鼓风机", "鼓风机吱呀吱哟哟地转", [
    c.ItemType("create:encased_fan", 1)
], [
    c.ItemType("create:encased_fan", 3)
]))
c1g.add_edge("mechanical press", "encased fan")
c1g.add_edge("get andesite alloy", "encased fan")

c1g.add_node(c.Node("fan catalyst", "鼓风机触媒", "你说为什么岩浆能往下流的非要往侧面流呢", [
    c.ItemType("create_connected:empty_fan_catalyst", 1)
], [
    c.ItemType("create:brass_ingot", 32)
]))
c1g.add_edge("encased fan", "fan catalyst")
c1g.add_edge("get brass", "fan catalyst")

c1g.add_node(c.Node("andesite funnel", "安山漏斗", "", [
    c.ItemType("create:andesite_funnel", 1)
], [
    c.ItemType("create:andesite_funnel", 2)
]))
c1g.add_edge("get andesite alloy", "andesite funnel")
c1g.add_edge("get kelps", "andesite funnel")

c1g.add_node(c.Node("brass funnel", "黄铜漏斗", "", [
    c.ItemType("create:brass_funnel", 1)
], [
    c.ItemType("create:brass_funnel", 2)
]))
c1g.add_edge("get kelps", "brass funnel")
c1g.add_edge("get brass", "brass funnel")

c1g.add_node(c.Node("chute", "溜槽", "已经不算慢了（", [
    c.ItemType("create:chute", 1)
], [
    c.ItemType("create:chute", 8)
]))
c1g.add_edge("mechanical press", "chute")

c1g.add_node(c.Node("smart chute", "智能溜槽", "", [
    c.ItemType("create:smart_chute", 1)
], [
    c.ItemType("create:smart_chute", 2)
]))
c1g.add_edge("chute", "smart chute")
c1g.add_edge("get brass", "smart chute")

c1g.add_node(c.Node("item vault", "保险库", "保险在哪", [
    c.ItemType("create:item_vault", 1)
], [
    c.ItemType("create:item_vault", 2)
]))
c1g.add_edge("mechanical press", "item vault")

c1g.add_node(c.Node("chain conveyor", "锁链传动轮", "", [
    c.ItemType("create:chain_conveyor", 1)
], [
    c.ItemType("create:chain_conveyor", 4)
]))
c1g.add_edge("get andesite alloy", "chain conveyor")

c1g.add_node(c.Node("packager", "打包机", "", [
    c.ItemType("create:packager", 1)
], [
    c.ItemType("create:packager", 2)
]))
c1g.add_edge("chain conveyor", "packager")

c1g.add_node(c.Node("package frogport", "货物蛙港", "不要成为蛙港仙人", [
    c.ItemType("create:package_frogport", 1)
], [
    c.ItemType("create:package_frogport", 2)
]))
c1g.add_edge("packager", "package frogport")
c1g.add_edge("get slimeballs", "package frogport")

c1g.add_node(c.Node("fluid pipe and pump", "流体管道与动力泵", "流体与动力学", [
    c.ItemType("create:mechanical_pump", 1),
    c.ItemType("create:fluid_pipe", 8)
], [
    c.ItemType("create:mechanical_pump", 2),
    c.ItemType("create:fluid_pipe", 32)
]))
c1g.add_edge("get coppers", "fluid pipe and pump")
c1g.add_edge("mechanical press", "fluid pipe and pump")

c1g.add_node(c.Node("steam engine", "蒸汽引擎", "真正的动力源！", [
    c.ItemType("create:steam_engine", 1)
], [
    c.ItemType("create:steam_engine", 4)
]))
c1g.add_edge("fluid tank", "steam engine")
c1g.add_edge("blaze burner", "steam engine")
c1g.add_edge("fluid pipe and pump", "steam engine")


with open("第一章：机械与资源.snbt", "w", encoding="utf-8") as f:
    f.write(slib.dumps(c.convert(c1g)))
