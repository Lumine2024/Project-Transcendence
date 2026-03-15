export namespace AlchemyMultiblock {
    export const controller: Internal.Block_ = "projecte:dm_pedestal";
    export const requiredBlocks: Internal.Block_[] = [
        "minecraft:coal_block",
        "minecraft:iron_block",
        "minecraft:gold_block",
        "minecraft:diamond_block",
        "minecraft:emerald_block",
        "minecraft:netherite_block",
        "projecte:dark_matter_block",
        "projecte:red_matter_block"
    ];
    export const centerBlock: Internal.Block_ = "minecraft:water";
    export const controllerStoreKey = "dm_pedestal_key";
}
