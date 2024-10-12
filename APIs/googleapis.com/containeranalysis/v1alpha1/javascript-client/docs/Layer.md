# ContainerAnalysisApi.Layer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_arguments** | **String** | The recovered arguments to the Dockerfile directive. | [optional] 
**directive** | **String** | The recovered Dockerfile directive used to construct this layer. | [optional] 



## Enum: DirectiveEnum


* `DIRECTIVE_UNSPECIFIED` (value: `"DIRECTIVE_UNSPECIFIED"`)

* `MAINTAINER` (value: `"MAINTAINER"`)

* `RUN` (value: `"RUN"`)

* `CMD` (value: `"CMD"`)

* `LABEL` (value: `"LABEL"`)

* `EXPOSE` (value: `"EXPOSE"`)

* `ENV` (value: `"ENV"`)

* `ADD` (value: `"ADD"`)

* `COPY` (value: `"COPY"`)

* `ENTRYPOINT` (value: `"ENTRYPOINT"`)

* `VOLUME` (value: `"VOLUME"`)

* `USER` (value: `"USER"`)

* `WORKDIR` (value: `"WORKDIR"`)

* `ARG` (value: `"ARG"`)

* `ONBUILD` (value: `"ONBUILD"`)

* `STOPSIGNAL` (value: `"STOPSIGNAL"`)

* `HEALTHCHECK` (value: `"HEALTHCHECK"`)

* `SHELL` (value: `"SHELL"`)




