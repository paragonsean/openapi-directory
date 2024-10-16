QT += network

HEADERS += \
# Models
    $${PWD}/OAIArchivedResult.h \
    $${PWD}/OAIAvailabilityRequest.h \
    $${PWD}/OAIAvailabilityResults.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAISnapshot.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIArchivedResult.cpp \
    $${PWD}/OAIAvailabilityRequest.cpp \
    $${PWD}/OAIAvailabilityResults.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAISnapshot.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
