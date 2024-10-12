QT += network

HEADERS += \
# Models
    $${PWD}/OAIAvsAddress.h \
    $${PWD}/OAICreateTestCardRangesRequest.h \
    $${PWD}/OAICreateTestCardRangesResult.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAITestCardRange.h \
    $${PWD}/OAITestCardRangeCreationResult.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
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
    $${PWD}/OAIAvsAddress.cpp \
    $${PWD}/OAICreateTestCardRangesRequest.cpp \
    $${PWD}/OAICreateTestCardRangesResult.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAITestCardRange.cpp \
    $${PWD}/OAITestCardRangeCreationResult.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
