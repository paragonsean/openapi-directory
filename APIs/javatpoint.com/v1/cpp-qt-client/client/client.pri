QT += network

HEADERS += \
# Models
    $${PWD}/OAIAndroidConfig.h \
    $${PWD}/OAIAndroidFcmOptions.h \
    $${PWD}/OAIAndroidNotification.h \
    $${PWD}/OAIApnsConfig.h \
    $${PWD}/OAIApnsFcmOptions.h \
    $${PWD}/OAIColor.h \
    $${PWD}/OAIFcmOptions.h \
    $${PWD}/OAILightSettings.h \
    $${PWD}/OAIMessage.h \
    $${PWD}/OAINotification.h \
    $${PWD}/OAISendMessageRequest.h \
    $${PWD}/OAIWebpushConfig.h \
    $${PWD}/OAIWebpushFcmOptions.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIAndroidConfig.cpp \
    $${PWD}/OAIAndroidFcmOptions.cpp \
    $${PWD}/OAIAndroidNotification.cpp \
    $${PWD}/OAIApnsConfig.cpp \
    $${PWD}/OAIApnsFcmOptions.cpp \
    $${PWD}/OAIColor.cpp \
    $${PWD}/OAIFcmOptions.cpp \
    $${PWD}/OAILightSettings.cpp \
    $${PWD}/OAIMessage.cpp \
    $${PWD}/OAINotification.cpp \
    $${PWD}/OAISendMessageRequest.cpp \
    $${PWD}/OAIWebpushConfig.cpp \
    $${PWD}/OAIWebpushFcmOptions.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
