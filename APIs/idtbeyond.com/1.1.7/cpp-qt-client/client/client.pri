QT += network

HEADERS += \
# Models
    $${PWD}/OAITopups.h \
    $${PWD}/OAITopupsReports.h \
    $${PWD}/OAITopupsReversal.h \
# APIs
    $${PWD}/OAIAccountApi.h \
    $${PWD}/OAIChargesApi.h \
    $${PWD}/OAIProductsApi.h \
    $${PWD}/OAITopupsApi.h \
    $${PWD}/OAIUtilitiesApi.h \
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
    $${PWD}/OAITopups.cpp \
    $${PWD}/OAITopupsReports.cpp \
    $${PWD}/OAITopupsReversal.cpp \
# APIs
    $${PWD}/OAIAccountApi.cpp \
    $${PWD}/OAIChargesApi.cpp \
    $${PWD}/OAIProductsApi.cpp \
    $${PWD}/OAITopupsApi.cpp \
    $${PWD}/OAIUtilitiesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
