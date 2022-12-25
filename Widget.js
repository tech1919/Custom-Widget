define(['dojo/_base/declare', 'jimu/BaseWidget','dojo/on'],
function(declare, BaseWidget) {
  //To create a widget, you need to derive from BaseWidget.
  return declare([BaseWidget], {
    name: 'limitations',

    startup: function(){
      

      console.log('startup limitations');
      console.log(this.sceneView.zoom);
      
      
    },
    
    _leftMouseClick:function(){
      var currZoom = this.sceneView.zoom;

      console.log("_leftMouseClick");
      
      console.log(this.sceneView);
      if(currZoom < 12){
        this.sceneView.zoom = 12;
      }
    },
  }); 
});