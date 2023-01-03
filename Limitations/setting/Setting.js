
define([
    'dojo/_base/declare',
    'jimu/BaseWidgetSetting'
  ],
  function(declare, BaseWidgetSetting) {
      return declare([BaseWidgetSetting], {
  
      postCreate: function(){
        //the config object is passed in
        this.setConfig(this.config);
      },
  
      setConfig: function(config){
        this.zoomConfig.value = config.zoomLimitedValue;
        this.tiltConfig.value = config.tiltLimitedValue;
        console.log("Zoom setConfig: " + config.zoomLimitedValue);
        console.log("Tilt setConfig: " + config.tiltLimitedValue);

      },
  
      getConfig: function(){
        //WAB will get config object through this method
        return {
          zoomLimitedValue: this.zoomConfig.value,
          tiltLimitedValue: this.tiltConfig.value
        };
      }
    });
  });