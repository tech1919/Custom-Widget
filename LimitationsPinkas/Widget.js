define(['dojo/_base/declare', 'jimu/BaseWidget','dojo/on', 'dojo/sniff'],
function(declare, BaseWidget) {
  //To create a widget, you need to derive from BaseWidget.
  return declare([BaseWidget], {
    name: 'limitations',

    startup: function(){
      var sceneElements = document.getElementsByClassName("esri-view-root");

      sceneElements[0].addEventListener('mousewheel', (event) => {
        this._zoomLimited()
      });
      sceneElements[0].addEventListener('click', (event) => {
        this._navigateLimited()
      });   
      
    },  
    _zoomLimited: function(){
      var currentZoom = Number(this.sceneView.zoom).toFixed(4);
      var limitZoomValue = 19.33;
      
      if(currentZoom > limitZoomValue){
        this.sceneView.zoom = limitZoomValue;
      }
      
    },
    _navigateLimited: function(){
      var limitTiltValue = 55;
      var currentTilt = this.sceneView.camera.tilt;
      var newCam = this.sceneView.camera.clone();
      newCam.tilt = limitTiltValue;
      

      if(currentTilt > limitTiltValue){
          this.sceneView.camera = newCam;
      }
    },
      
  }); 
});