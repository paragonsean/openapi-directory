# BatchApi.Script

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **String** | Script file path on the host VM. To specify an interpreter, please add a &#x60;#!&#x60;(also known as [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix))) as the first line of the file.(For example, to execute the script using bash, &#x60;#!/bin/bash&#x60; should be the first line of the file. To execute the script using&#x60;Python3&#x60;, &#x60;#!/usr/bin/env python3&#x60; should be the first line of the file.) Otherwise, the file will by default be executed by &#x60;/bin/sh&#x60;. | [optional] 
**text** | **String** | Shell script text. To specify an interpreter, please add a &#x60;#!\\n&#x60; at the beginning of the text.(For example, to execute the script using bash, &#x60;#!/bin/bash\\n&#x60; should be added. To execute the script using&#x60;Python3&#x60;, &#x60;#!/usr/bin/env python3\\n&#x60; should be added.) Otherwise, the script will by default be executed by &#x60;/bin/sh&#x60;. | [optional] 


