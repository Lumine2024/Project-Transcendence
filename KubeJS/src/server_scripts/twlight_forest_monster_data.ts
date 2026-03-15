const modifyAttackDamage = (entity: Internal.LivingEntity, value: number): boolean => {
    const attackDamage = entity.getAttribute("minecraft:generic.attack_damage" as any);
    if(!attackDamage) return false;
    attackDamage.setBaseValue(value);
    return true;
}
const modifyArmor = (entity: Internal.LivingEntity, value: number): boolean => {
    const armor = entity.getAttribute("minecraft:generic.armor" as any);
    if(!armor) return false;
    armor.setBaseValue(value);
    return true;
}

EntityEvents.spawned(event => {
    const entity = event.entity as any as Internal.LivingEntity;
    if(!entity.living) return;
    if(entity.type == "twlightforest:naga") {
        if(!modifyAttackDamage(entity, 20)) {
            event.server.players.forEach(player => {
                player.tell("naga don't have attack damage" as any);
            });
        }
        if(!modifyArmor(entity, 20)) {
            event.server.players.forEach(player => {
                player.tell("naga don't have defence" as any);
            });
        }
    }
});