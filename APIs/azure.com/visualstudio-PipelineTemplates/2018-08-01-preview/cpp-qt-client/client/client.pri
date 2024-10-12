QT += network

HEADERS += \
# Models
    $${PWD}/OAIInputDescriptor.h \
    $${PWD}/OAIInputValue.h \
    $${PWD}/OAIPipelineTemplate.h \
    $${PWD}/OAIPipelineTemplateResourceListResult.h \
# APIs
    $${PWD}/OAIPipelineTemplatesApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIInputDescriptor.cpp \
    $${PWD}/OAIInputValue.cpp \
    $${PWD}/OAIPipelineTemplate.cpp \
    $${PWD}/OAIPipelineTemplateResourceListResult.cpp \
# APIs
    $${PWD}/OAIPipelineTemplatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
