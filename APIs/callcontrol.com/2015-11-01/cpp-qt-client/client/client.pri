QT += network

HEADERS += \
# Models
    $${PWD}/OAICallControlUser.h \
    $${PWD}/OAICallReport.h \
    $${PWD}/OAIComplaints.h \
    $${PWD}/OAIQuietHour.h \
    $${PWD}/OAIReputation.h \
# APIs
    $${PWD}/OAIComplaintsApi.h \
    $${PWD}/OAIEnterpriseApiApi.h \
    $${PWD}/OAIReputationApi.h \
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
    $${PWD}/OAICallControlUser.cpp \
    $${PWD}/OAICallReport.cpp \
    $${PWD}/OAIComplaints.cpp \
    $${PWD}/OAIQuietHour.cpp \
    $${PWD}/OAIReputation.cpp \
# APIs
    $${PWD}/OAIComplaintsApi.cpp \
    $${PWD}/OAIEnterpriseApiApi.cpp \
    $${PWD}/OAIReputationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
