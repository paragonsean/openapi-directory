QT += network

HEADERS += \
# Models
    $${PWD}/OAICodeSample.h \
    $${PWD}/OAIDocument.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIFacet.h \
    $${PWD}/OAI_application_newID_get_200_response.h \
    $${PWD}/OAI_application_newID_get_403_response.h \
    $${PWD}/OAI_application_status_get_200_response.h \
    $${PWD}/OAI_application_status_get_500_response.h \
# APIs
    $${PWD}/OAIApplicationApi.h \
    $${PWD}/OAICodeSamplesApi.h \
    $${PWD}/OAIDocumentsApi.h \
    $${PWD}/OAIFacetsApi.h \
    $${PWD}/OAISearchApi.h \
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
    $${PWD}/OAICodeSample.cpp \
    $${PWD}/OAIDocument.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIFacet.cpp \
    $${PWD}/OAI_application_newID_get_200_response.cpp \
    $${PWD}/OAI_application_newID_get_403_response.cpp \
    $${PWD}/OAI_application_status_get_200_response.cpp \
    $${PWD}/OAI_application_status_get_500_response.cpp \
# APIs
    $${PWD}/OAIApplicationApi.cpp \
    $${PWD}/OAICodeSamplesApi.cpp \
    $${PWD}/OAIDocumentsApi.cpp \
    $${PWD}/OAIFacetsApi.cpp \
    $${PWD}/OAISearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
