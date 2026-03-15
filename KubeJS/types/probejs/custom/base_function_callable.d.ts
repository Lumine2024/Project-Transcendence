declare namespace Internal {
    interface RecipeTypeFunction {
        (result: OutputItem_, pattern: string[], key: { [key: string]: InputItem_ }): Special.Recipes.ShapedKubejs;
        (result: OutputItem_, ingredients: InputItem_[][]): Special.Recipes.ShapedKubejs;
        (...args: any[]): any;
    }
}