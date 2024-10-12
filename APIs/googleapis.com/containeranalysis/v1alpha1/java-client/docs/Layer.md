

# Layer

Layer holds metadata specific to a layer of a Docker image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | **String** | The recovered arguments to the Dockerfile directive. |  [optional] |
|**directive** | [**DirectiveEnum**](#DirectiveEnum) | The recovered Dockerfile directive used to construct this layer. |  [optional] |



## Enum: DirectiveEnum

| Name | Value |
|---- | -----|
| DIRECTIVE_UNSPECIFIED | &quot;DIRECTIVE_UNSPECIFIED&quot; |
| MAINTAINER | &quot;MAINTAINER&quot; |
| RUN | &quot;RUN&quot; |
| CMD | &quot;CMD&quot; |
| LABEL | &quot;LABEL&quot; |
| EXPOSE | &quot;EXPOSE&quot; |
| ENV | &quot;ENV&quot; |
| ADD | &quot;ADD&quot; |
| COPY | &quot;COPY&quot; |
| ENTRYPOINT | &quot;ENTRYPOINT&quot; |
| VOLUME | &quot;VOLUME&quot; |
| USER | &quot;USER&quot; |
| WORKDIR | &quot;WORKDIR&quot; |
| ARG | &quot;ARG&quot; |
| ONBUILD | &quot;ONBUILD&quot; |
| STOPSIGNAL | &quot;STOPSIGNAL&quot; |
| HEALTHCHECK | &quot;HEALTHCHECK&quot; |
| SHELL | &quot;SHELL&quot; |



