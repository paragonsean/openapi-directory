QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiResponse.h \
    $${PWD}/OAIQueue.h \
    $${PWD}/OAIQueueMessage.h \
# APIs
    $${PWD}/OAIQueuesApi.h \
    $${PWD}/OAIStatusApi.h \
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
    $${PWD}/OAIApiResponse.cpp \
    $${PWD}/OAIQueue.cpp \
    $${PWD}/OAIQueueMessage.cpp \
# APIs
    $${PWD}/OAIQueuesApi.cpp \
    $${PWD}/OAIStatusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
