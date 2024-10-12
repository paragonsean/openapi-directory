QT += network

HEADERS += \
# Models
    $${PWD}/OAICountry.h \
    $${PWD}/OAICountrySummary.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorField.h \
    $${PWD}/OAIErrorLimit.h \
    $${PWD}/OAIState.h \
# APIs
    $${PWD}/OAIV1Api.h \
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
    $${PWD}/OAICountry.cpp \
    $${PWD}/OAICountrySummary.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorField.cpp \
    $${PWD}/OAIErrorLimit.cpp \
    $${PWD}/OAIState.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
