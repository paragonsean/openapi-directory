QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetAllContentTypes_200_response.h \
    $${PWD}/OAIGetAllContentTypes_200_response_contentTypes_inner.h \
    $${PWD}/OAIGetAllContentTypes_200_response_contentTypes_inner_configurationSchemaSets_inner.h \
    $${PWD}/OAIGetCMSpage_200_response.h \
    $${PWD}/OAIGetCMSpage_200_response_sections_inner.h \
    $${PWD}/OAIGetPagesbyContentType_200_response.h \
    $${PWD}/OAIGetPagesbyContentType_200_response_data_inner.h \
    $${PWD}/OAIGetPagesbyContentType_200_response_data_inner_sections_inner.h \
# APIs
    $${PWD}/OAIPagesApi.h \
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
    $${PWD}/OAIGetAllContentTypes_200_response.cpp \
    $${PWD}/OAIGetAllContentTypes_200_response_contentTypes_inner.cpp \
    $${PWD}/OAIGetAllContentTypes_200_response_contentTypes_inner_configurationSchemaSets_inner.cpp \
    $${PWD}/OAIGetCMSpage_200_response.cpp \
    $${PWD}/OAIGetCMSpage_200_response_sections_inner.cpp \
    $${PWD}/OAIGetPagesbyContentType_200_response.cpp \
    $${PWD}/OAIGetPagesbyContentType_200_response_data_inner.cpp \
    $${PWD}/OAIGetPagesbyContentType_200_response_data_inner_sections_inner.cpp \
# APIs
    $${PWD}/OAIPagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
