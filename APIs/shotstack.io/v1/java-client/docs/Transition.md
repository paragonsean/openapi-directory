

# Transition

In and out transitions for a clip - i.e. fade in and fade out

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**in** | [**InEnum**](#InEnum) | The transition in. Available transitions are:   &lt;ul&gt;     &lt;li&gt;&#x60;fade&#x60; - fade in&lt;/li&gt;     &lt;li&gt;&#x60;reveal&#x60; - reveal from left to right&lt;/li&gt;     &lt;li&gt;&#x60;wipeLeft&#x60; - fade across screen to the left&lt;/li&gt;     &lt;li&gt;&#x60;wipeRight&#x60; - fade across screen to the right&lt;/li&gt;     &lt;li&gt;&#x60;slideLeft&#x60; - move slightly left and fade in&lt;/li&gt;     &lt;li&gt;&#x60;slideRight&#x60; - move slightly right and fade in&lt;/li&gt;     &lt;li&gt;&#x60;slideUp&#x60; - move slightly up and fade in&lt;/li&gt;     &lt;li&gt;&#x60;slideDown&#x60; - move slightly down and fade in&lt;/li&gt;     &lt;li&gt;&#x60;carouselLeft&#x60; - slide in from right to left&lt;/li&gt;     &lt;li&gt;&#x60;carouselRight&#x60; - slide in from left to right&lt;/li&gt;     &lt;li&gt;&#x60;carouselUp&#x60; - slide in from bottom to top&lt;/li&gt;     &lt;li&gt;&#x60;carouselDown&#x60; - slide in from top to bottom&lt;/li&gt;     &lt;li&gt;&#x60;shuffleTopRight&#x60; - rotate in from top right&lt;/li&gt;     &lt;li&gt;&#x60;shuffleRightTop&#x60; - rotate in from right top&lt;/li&gt;     &lt;li&gt;&#x60;shuffleRightBottom&#x60; - rotate in from right bottom&lt;/li&gt;     &lt;li&gt;&#x60;shuffleBottomRight&#x60; - rotate in from bottom right&lt;/li&gt;     &lt;li&gt;&#x60;shuffleBottomLeft&#x60; - rotate in from bottom left&lt;/li&gt;     &lt;li&gt;&#x60;shuffleLeftBottom&#x60; - rotate in from left bottom&lt;/li&gt;     &lt;li&gt;&#x60;shuffleLeftTop&#x60; - rotate in from left top&lt;/li&gt;     &lt;li&gt;&#x60;shuffleTopLeft&#x60; - rotate in from top left&lt;/li&gt;     &lt;li&gt;&#x60;zoom&#x60; - fast zoom in&lt;/li&gt;   &lt;/ul&gt; The transition speed can also be controlled by appending &#x60;Fast&#x60; or &#x60;Slow&#x60; to the transition, e.g. &#x60;fadeFast&#x60; or &#x60;CarouselLeftSlow&#x60;. |  [optional] |
|**out** | [**OutEnum**](#OutEnum) | The transition out. Available transitions are:   &lt;ul&gt;     &lt;li&gt;&#x60;fade&#x60; - fade out&lt;/li&gt;     &lt;li&gt;&#x60;reveal&#x60; - reveal from right to left&lt;/li&gt;     &lt;li&gt;&#x60;wipeLeft&#x60; - fade across screen to the left&lt;/li&gt;     &lt;li&gt;&#x60;wipeRight&#x60; - fade across screen to the right&lt;/li&gt;     &lt;li&gt;&#x60;slideLeft&#x60; - move slightly left and fade out&lt;/li&gt;     &lt;li&gt;&#x60;slideRight&#x60; - move slightly right and fade out&lt;/li&gt;     &lt;li&gt;&#x60;slideUp&#x60; - move slightly up and fade out&lt;/li&gt;     &lt;li&gt;&#x60;slideDown&#x60; - move slightly down and fade out&lt;/li&gt;     &lt;li&gt;&#x60;carouselLeft&#x60; - slide out from right to left&lt;/li&gt;     &lt;li&gt;&#x60;carouselRight&#x60; - slide out from left to right&lt;/li&gt;     &lt;li&gt;&#x60;carouselUp&#x60; - slide out from bottom to top&lt;/li&gt;     &lt;li&gt;&#x60;carouselDown&#x60; - slide out from top  to bottom&lt;/li&gt;     &lt;li&gt;&#x60;shuffleTopRight&#x60; - rotate out from top right&lt;/li&gt;     &lt;li&gt;&#x60;shuffleRightTop&#x60; - rotate out from right top&lt;/li&gt;     &lt;li&gt;&#x60;shuffleRightBottom&#x60; - rotate out from right bottom&lt;/li&gt;     &lt;li&gt;&#x60;shuffleBottomRight&#x60; - rotate out from bottom right&lt;/li&gt;     &lt;li&gt;&#x60;shuffleBottomLeft&#x60; - rotate out from bottom left&lt;/li&gt;     &lt;li&gt;&#x60;shuffleLeftBottom&#x60; - rotate out from left bottom&lt;/li&gt;     &lt;li&gt;&#x60;shuffleLeftTop&#x60; - rotate out from left top&lt;/li&gt;     &lt;li&gt;&#x60;shuffleTopLeft&#x60; - rotate out from top left&lt;/li&gt;     &lt;li&gt;&#x60;zoom&#x60; - fast zoom out&lt;/li&gt;   &lt;/ul&gt; The transition speed can also be controlled by appending &#x60;Fast&#x60; or &#x60;Slow&#x60; to the transition, e.g. &#x60;fadeFast&#x60; or &#x60;CarouselLeftSlow&#x60;. |  [optional] |



## Enum: InEnum

| Name | Value |
|---- | -----|
| FADE | &quot;fade&quot; |
| FADE_SLOW | &quot;fadeSlow&quot; |
| FADE_FAST | &quot;fadeFast&quot; |
| REVEAL | &quot;reveal&quot; |
| REVEAL_SLOW | &quot;revealSlow&quot; |
| REVEAL_FAST | &quot;revealFast&quot; |
| WIPE_LEFT | &quot;wipeLeft&quot; |
| WIPE_LEFT_SLOW | &quot;wipeLeftSlow&quot; |
| WIPE_LEFT_FAST | &quot;wipeLeftFast&quot; |
| WIPE_RIGHT | &quot;wipeRight&quot; |
| WIPE_RIGHT_SLOW | &quot;wipeRightSlow&quot; |
| WIPE_RIGHT_FAST | &quot;wipeRightFast&quot; |
| SLIDE_LEFT | &quot;slideLeft&quot; |
| SLIDE_LEFT_SLOW | &quot;slideLeftSlow&quot; |
| SLIDE_LEFT_FAST | &quot;slideLeftFast&quot; |
| SLIDE_RIGHT | &quot;slideRight&quot; |
| SLIDE_RIGHT_SLOW | &quot;slideRightSlow&quot; |
| SLIDE_RIGHT_FAST | &quot;slideRightFast&quot; |
| SLIDE_UP | &quot;slideUp&quot; |
| SLIDE_UP_SLOW | &quot;slideUpSlow&quot; |
| SLIDE_UP_FAST | &quot;slideUpFast&quot; |
| SLIDE_DOWN | &quot;slideDown&quot; |
| SLIDE_DOWN_SLOW | &quot;slideDownSlow&quot; |
| SLIDE_DOWN_FAST | &quot;slideDownFast&quot; |
| CAROUSEL_LEFT | &quot;carouselLeft&quot; |
| CAROUSEL_LEFT_SLOW | &quot;carouselLeftSlow&quot; |
| CAROUSEL_LEFT_FAST | &quot;carouselLeftFast&quot; |
| CAROUSEL_RIGHT | &quot;carouselRight&quot; |
| CAROUSEL_RIGHT_SLOW | &quot;carouselRightSlow&quot; |
| CAROUSEL_RIGHT_FAST | &quot;carouselRightFast&quot; |
| CAROUSEL_UP | &quot;carouselUp&quot; |
| CAROUSEL_UP_SLOW | &quot;carouselUpSlow&quot; |
| CAROUSEL_UP_FAST | &quot;carouselUpFast&quot; |
| CAROUSEL_DOWN | &quot;carouselDown&quot; |
| CAROUSEL_DOWN_SLOW | &quot;carouselDownSlow&quot; |
| CAROUSEL_DOWN_FAST | &quot;carouselDownFast&quot; |
| SHUFFLE_TOP_RIGHT | &quot;shuffleTopRight&quot; |
| SHUFFLE_TOP_RIGHT_SLOW | &quot;shuffleTopRightSlow&quot; |
| SHUFFLE_TOP_RIGHT_FAST | &quot;shuffleTopRightFast&quot; |
| SHUFFLE_RIGHT_TOP | &quot;shuffleRightTop&quot; |
| SHUFFLE_RIGHT_TOP_SLOW | &quot;shuffleRightTopSlow&quot; |
| SHUFFLE_RIGHT_TOP_FAST | &quot;shuffleRightTopFast&quot; |
| SHUFFLE_RIGHT_BOTTOM | &quot;shuffleRightBottom&quot; |
| SHUFFLE_RIGHT_BOTTOM_SLOW | &quot;shuffleRightBottomSlow&quot; |
| SHUFFLE_RIGHT_BOTTOM_FAST | &quot;shuffleRightBottomFast&quot; |
| SHUFFLE_BOTTOM_RIGHT | &quot;shuffleBottomRight&quot; |
| SHUFFLE_BOTTOM_RIGHT_SLOW | &quot;shuffleBottomRightSlow&quot; |
| SHUFFLE_BOTTOM_RIGHT_FAST | &quot;shuffleBottomRightFast&quot; |
| SHUFFLE_BOTTOM_LEFT | &quot;shuffleBottomLeft&quot; |
| SHUFFLE_BOTTOM_LEFT_SLOW | &quot;shuffleBottomLeftSlow&quot; |
| SHUFFLE_BOTTOM_LEFT_FAST | &quot;shuffleBottomLeftFast&quot; |
| SHUFFLE_LEFT_BOTTOM | &quot;shuffleLeftBottom&quot; |
| SHUFFLE_LEFT_BOTTOM_SLOW | &quot;shuffleLeftBottomSlow&quot; |
| SHUFFLE_LEFT_BOTTOM_FAST | &quot;shuffleLeftBottomFast&quot; |
| SHUFFLE_LEFT_TOP | &quot;shuffleLeftTop&quot; |
| SHUFFLE_LEFT_TOP_SLOW | &quot;shuffleLeftTopSlow&quot; |
| SHUFFLE_LEFT_TOP_FAST | &quot;shuffleLeftTopFast&quot; |
| SHUFFLE_TOP_LEFT | &quot;shuffleTopLeft&quot; |
| SHUFFLE_TOP_LEFT_SLOW | &quot;shuffleTopLeftSlow&quot; |
| SHUFFLE_TOP_LEFT_FAST | &quot;shuffleTopLeftFast&quot; |
| ZOOM | &quot;zoom&quot; |



## Enum: OutEnum

| Name | Value |
|---- | -----|
| FADE | &quot;fade&quot; |
| FADE_SLOW | &quot;fadeSlow&quot; |
| FADE_FAST | &quot;fadeFast&quot; |
| REVEAL | &quot;reveal&quot; |
| REVEAL_SLOW | &quot;revealSlow&quot; |
| REVEAL_FAST | &quot;revealFast&quot; |
| WIPE_LEFT | &quot;wipeLeft&quot; |
| WIPE_LEFT_SLOW | &quot;wipeLeftSlow&quot; |
| WIPE_LEFT_FAST | &quot;wipeLeftFast&quot; |
| WIPE_RIGHT | &quot;wipeRight&quot; |
| WIPE_RIGHT_SLOW | &quot;wipeRightSlow&quot; |
| WIPE_RIGHT_FAST | &quot;wipeRightFast&quot; |
| SLIDE_LEFT | &quot;slideLeft&quot; |
| SLIDE_LEFT_SLOW | &quot;slideLeftSlow&quot; |
| SLIDE_LEFT_FAST | &quot;slideLeftFast&quot; |
| SLIDE_RIGHT | &quot;slideRight&quot; |
| SLIDE_RIGHT_SLOW | &quot;slideRightSlow&quot; |
| SLIDE_RIGHT_FAST | &quot;slideRightFast&quot; |
| SLIDE_UP | &quot;slideUp&quot; |
| SLIDE_UP_SLOW | &quot;slideUpSlow&quot; |
| SLIDE_UP_FAST | &quot;slideUpFast&quot; |
| SLIDE_DOWN | &quot;slideDown&quot; |
| SLIDE_DOWN_SLOW | &quot;slideDownSlow&quot; |
| SLIDE_DOWN_FAST | &quot;slideDownFast&quot; |
| CAROUSEL_LEFT | &quot;carouselLeft&quot; |
| CAROUSEL_LEFT_SLOW | &quot;carouselLeftSlow&quot; |
| CAROUSEL_LEFT_FAST | &quot;carouselLeftFast&quot; |
| CAROUSEL_RIGHT | &quot;carouselRight&quot; |
| CAROUSEL_RIGHT_SLOW | &quot;carouselRightSlow&quot; |
| CAROUSEL_RIGHT_FAST | &quot;carouselRightFast&quot; |
| CAROUSEL_UP | &quot;carouselUp&quot; |
| CAROUSEL_UP_SLOW | &quot;carouselUpSlow&quot; |
| CAROUSEL_UP_FAST | &quot;carouselUpFast&quot; |
| CAROUSEL_DOWN | &quot;carouselDown&quot; |
| CAROUSEL_DOWN_SLOW | &quot;carouselDownSlow&quot; |
| CAROUSEL_DOWN_FAST | &quot;carouselDownFast&quot; |
| SHUFFLE_TOP_RIGHT | &quot;shuffleTopRight&quot; |
| SHUFFLE_TOP_RIGHT_SLOW | &quot;shuffleTopRightSlow&quot; |
| SHUFFLE_TOP_RIGHT_FAST | &quot;shuffleTopRightFast&quot; |
| SHUFFLE_RIGHT_TOP | &quot;shuffleRightTop&quot; |
| SHUFFLE_RIGHT_TOP_SLOW | &quot;shuffleRightTopSlow&quot; |
| SHUFFLE_RIGHT_TOP_FAST | &quot;shuffleRightTopFast&quot; |
| SHUFFLE_RIGHT_BOTTOM | &quot;shuffleRightBottom&quot; |
| SHUFFLE_RIGHT_BOTTOM_SLOW | &quot;shuffleRightBottomSlow&quot; |
| SHUFFLE_RIGHT_BOTTOM_FAST | &quot;shuffleRightBottomFast&quot; |
| SHUFFLE_BOTTOM_RIGHT | &quot;shuffleBottomRight&quot; |
| SHUFFLE_BOTTOM_RIGHT_SLOW | &quot;shuffleBottomRightSlow&quot; |
| SHUFFLE_BOTTOM_RIGHT_FAST | &quot;shuffleBottomRightFast&quot; |
| SHUFFLE_BOTTOM_LEFT | &quot;shuffleBottomLeft&quot; |
| SHUFFLE_BOTTOM_LEFT_SLOW | &quot;shuffleBottomLeftSlow&quot; |
| SHUFFLE_BOTTOM_LEFT_FAST | &quot;shuffleBottomLeftFast&quot; |
| SHUFFLE_LEFT_BOTTOM | &quot;shuffleLeftBottom&quot; |
| SHUFFLE_LEFT_BOTTOM_SLOW | &quot;shuffleLeftBottomSlow&quot; |
| SHUFFLE_LEFT_BOTTOM_FAST | &quot;shuffleLeftBottomFast&quot; |
| SHUFFLE_LEFT_TOP | &quot;shuffleLeftTop&quot; |
| SHUFFLE_LEFT_TOP_SLOW | &quot;shuffleLeftTopSlow&quot; |
| SHUFFLE_LEFT_TOP_FAST | &quot;shuffleLeftTopFast&quot; |
| SHUFFLE_TOP_LEFT | &quot;shuffleTopLeft&quot; |
| SHUFFLE_TOP_LEFT_SLOW | &quot;shuffleTopLeftSlow&quot; |
| SHUFFLE_TOP_LEFT_FAST | &quot;shuffleTopLeftFast&quot; |
| ZOOM | &quot;zoom&quot; |



