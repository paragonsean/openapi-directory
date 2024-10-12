QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleBytestreamMedia.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIStatus.h \
# APIs
    $${PWD}/OAIMediaApi.h \
    $${PWD}/OAISdfdownloadtasksApi.h \
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
    $${PWD}/OAIGoogleBytestreamMedia.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIStatus.cpp \
# APIs
    $${PWD}/OAIMediaApi.cpp \
    $${PWD}/OAISdfdownloadtasksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
