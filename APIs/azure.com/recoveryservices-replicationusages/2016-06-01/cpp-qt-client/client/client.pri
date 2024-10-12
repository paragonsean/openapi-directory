QT += network

HEADERS += \
# Models
    $${PWD}/OAIJobsSummary.h \
    $${PWD}/OAIMonitoringSummary.h \
    $${PWD}/OAIReplicationUsage.h \
    $${PWD}/OAIReplicationUsageList.h \
# APIs
    $${PWD}/OAIReplicationUsagesApi.h \
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
    $${PWD}/OAIJobsSummary.cpp \
    $${PWD}/OAIMonitoringSummary.cpp \
    $${PWD}/OAIReplicationUsage.cpp \
    $${PWD}/OAIReplicationUsageList.cpp \
# APIs
    $${PWD}/OAIReplicationUsagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
