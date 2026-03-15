interface PonderJSSceneBuilder extends Internal.SceneBuilder {
    addKeyFrame(): void;
    showStructure(): void;
    text(arg0: number, content: string, pos: BlockPos | number[]): Internal.TextElementBuilder;
    get world(): {
        setBlock(pos: BlockPos | number[], block: Internal.Ingredient_, arg2: boolean);
    }
};