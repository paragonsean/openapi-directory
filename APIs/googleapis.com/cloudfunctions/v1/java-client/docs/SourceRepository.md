

# SourceRepository

Describes SourceRepository, used to represent parameters related to source repository where a function is hosted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployedUrl** | **String** | Output only. The URL pointing to the hosted repository where the function were defined at the time of deployment. It always points to a specific commit in the format described above. |  [optional] [readonly] |
|**url** | **String** | The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats: To refer to a specific commit: &#x60;https://source.developers.google.com/projects/_*_/repos/_*_/revisions/_*_/paths/_*&#x60; To refer to a moveable alias (branch): &#x60;https://source.developers.google.com/projects/_*_/repos/_*_/moveable-aliases/_*_/paths/_*&#x60; In particular, to refer to HEAD use &#x60;master&#x60; moveable alias. To refer to a specific fixed alias (tag): &#x60;https://source.developers.google.com/projects/_*_/repos/_*_/fixed-aliases/_*_/paths/_*&#x60; You may omit &#x60;paths/_*&#x60; if you want to use the main directory. |  [optional] |



