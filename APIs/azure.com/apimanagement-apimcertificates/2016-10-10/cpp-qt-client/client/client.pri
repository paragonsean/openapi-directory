QT += network

HEADERS += \
# Models
    $${PWD}/OAICertificateCollection.h \
    $${PWD}/OAICertificateContract.h \
    $${PWD}/OAICertificateCreateOrUpdateParameters.h \
    $${PWD}/OAICertificates_ListByService_default_response.h \
    $${PWD}/OAICertificates_ListByService_default_response_details_inner.h \
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
    $${PWD}/OAICertificateCollection.cpp \
    $${PWD}/OAICertificateContract.cpp \
    $${PWD}/OAICertificateCreateOrUpdateParameters.cpp \
    $${PWD}/OAICertificates_ListByService_default_response.cpp \
    $${PWD}/OAICertificates_ListByService_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAICertificatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
