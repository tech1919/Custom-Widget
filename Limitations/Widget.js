define(['dojo/_base/declare',
        'jimu/BaseWidget',
        'esri/views/View',
        'esri/Map'
      ],
function(declare, BaseWidget) {
  //To create a widget, you need to derive from BaseWidget.
  return declare([BaseWidget], {
    name: 'limitations',

    startup: function(){
      // currently is permanent numbers.
      // further will depend on the configuration! 
      const zoomLimit = 150;
      const tiltLimit = 70;
      // var sceneElement = document.getElementsByClassName("esri-view-root");


      // initialization constraints
      this.sceneView.constraints.tilt.max = tiltLimit;
      this.sceneView.constraints.altitude.min = zoomLimit;

      // console.log(this.sceneView.camera.position.z);
      // console.log(this.sceneView.camera.tilt);

      // If the map already after the limited values.
      if(this.sceneView.camera.position.z < zoomLimit){
        //CHANGE ZOOM:
        this.sceneView.goTo(
          {
            position:{
              z:zoomLimit,
            }
          });
      }
      if(this.sceneView.camera.tilt > tiltLimit){
        //CHANGE TILT:
        this.sceneView.goTo(
          {
            tilt : tiltLimit,
          });
      }

      sceneElement[0].addEventListener("mousewheel", (e) => {
        console.log(this.sceneView.camera.position.z);
        console.log(this.sceneView.camera.tilt);
        console.log(this.sceneView.zoom);
        
      })
      
    },
  
      
  }); 
});