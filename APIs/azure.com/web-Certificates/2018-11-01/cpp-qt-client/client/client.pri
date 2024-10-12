QT += network

HEADERS += \
# Models
    $${PWD}/OAICertificate.h \
    $${PWD}/OAICertificateCollection.h \
    $${PWD}/OAICertificatePatchResource.h \
    $${PWD}/OAICertificates_List_default_response.h \
    $${PWD}/OAICertificates_List_default_response_error.h \
    $${PWD}/OAICertificates_List_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAICertificatesApi.h \
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
    $${PWD}/OAICertificate.cpp \
    $${PWD}/OAICertificateCollection.cpp \
    $${PWD}/OAICertificatePatchResource.cpp \
    $${PWD}/OAICertificates_List_default_response.cpp \
    $${PWD}/OAICertificates_List_default_response_error.cpp \
    $${PWD}/OAICertificates_List_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAICertificatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
