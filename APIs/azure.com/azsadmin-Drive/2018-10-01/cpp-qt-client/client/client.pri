QT += network

HEADERS += \
# Models
    $${PWD}/OAIDrive.h \
    $${PWD}/OAIDriveList.h \
    $${PWD}/OAIDriveModel.h \
# APIs
    $${PWD}/OAIDrivesApi.h \
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
    $${PWD}/OAIDrive.cpp \
    $${PWD}/OAIDriveList.cpp \
    $${PWD}/OAIDriveModel.cpp \
# APIs
    $${PWD}/OAIDrivesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
