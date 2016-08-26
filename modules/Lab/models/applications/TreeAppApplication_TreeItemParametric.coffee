class TreeAppApplication_TreeItemParametric extends TreeAppApplication
    constructor: ->
        super()
        
        @name = 'TreeItem Parametric'
        @powered_with    = 'SpinalCom'
        @description = 'Insert a new TreeItem Parametric in the session.'
            
        @actions.push
            txt: "TreeItem Parametric"
            fun: ( evt, app ) =>
                app.undo_manager.snapshot()
                instance = @add_item_depending_selected_tree app.data, TreeItem_Parametric, (object) =>
                    name = prompt "Enter the name of the TreeItem:"
                    if name
                        object._name.set name
                    else
                        object._name.set "Item"
        
        
            