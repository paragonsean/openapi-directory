QT += network

HEADERS += \
# Models
    $${PWD}/OAIBalancePlatformNotificationResponse.h \
    $${PWD}/OAIReportNotificationData.h \
    $${PWD}/OAIReportNotificationRequest.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceReference.h \
# APIs
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
    $${PWD}/OAIBalancePlatformNotificationResponse.cpp \
    $${PWD}/OAIReportNotificationData.cpp \
    $${PWD}/OAIReportNotificationRequest.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceReference.cpp \
# APIs
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
