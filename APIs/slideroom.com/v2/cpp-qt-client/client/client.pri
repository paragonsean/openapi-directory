QT += network

HEADERS += \
# Models
    $${PWD}/OAIExportResultV2.h \
    $${PWD}/OAIRequestApplicationExportResultV2.h \
# APIs
    $${PWD}/OAIApplicantApi.h \
    $${PWD}/OAIApplicationApi.h \
    $${PWD}/OAIExportApi.h \
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
    $${PWD}/OAIExportResultV2.cpp \
    $${PWD}/OAIRequestApplicationExportResultV2.cpp \
# APIs
    $${PWD}/OAIApplicantApi.cpp \
    $${PWD}/OAIApplicationApi.cpp \
    $${PWD}/OAIExportApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
