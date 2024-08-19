# RocketServices.AppConfigPlayback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chainPlayCountdown** | **Number** | The number of seconds before autoplay of next video.  If set to 0 there will be no autoplay.  | 
**chainPlaySqueezeback** | **Number** | The number of seconds before the end of playback when the current video should be minimized and user options are presented within the video player.  If set to 0 there will be no squeezeback.  | 
**chainPlayTimeout** | **Number** | The number of minutes of user inactivity before autoplay is paused.  If set to 0 there will be no autoplay timeout.  | 
**heartbeatFrequency** | **Number** | How often a heartbeat should be renewed during playback. | 
**viewEventPoints** | **[Number]** | An array of percentage points in which to fire off plabyack view events. For example a value of 0.5 would indicate that an event should be fired when the user is half way through the video. Often known as quartiles when four equaly spread event points.  | 


