QT += network

HEADERS += \
# Models
    $${PWD}/OAI_render__templateId__post_200_response.h \
    $${PWD}/OAI_render__templateId__post_200_response_data.h \
    $${PWD}/OAI_render__templateId__post_request.h \
    $${PWD}/OAI_status_get_200_response.h \
    $${PWD}/OAI_template__templateId__delete_200_response.h \
    $${PWD}/OAI_template_post_200_response.h \
    $${PWD}/OAI_template_post_200_response_data.h \
    $${PWD}/OAI_template_post_request.h \
# APIs
    $${PWD}/OAIRenderApi.h \
    $${PWD}/OAIStatusApi.h \
    $${PWD}/OAITemplateApi.h \
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
    $${PWD}/OAI_render__templateId__post_200_response.cpp \
    $${PWD}/OAI_render__templateId__post_200_response_data.cpp \
    $${PWD}/OAI_render__templateId__post_request.cpp \
    $${PWD}/OAI_status_get_200_response.cpp \
    $${PWD}/OAI_template__templateId__delete_200_response.cpp \
    $${PWD}/OAI_template_post_200_response.cpp \
    $${PWD}/OAI_template_post_200_response_data.cpp \
    $${PWD}/OAI_template_post_request.cpp \
# APIs
    $${PWD}/OAIRenderApi.cpp \
    $${PWD}/OAIStatusApi.cpp \
    $${PWD}/OAITemplateApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
