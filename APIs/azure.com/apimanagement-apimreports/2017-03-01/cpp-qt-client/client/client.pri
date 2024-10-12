QT += network

HEADERS += \
# Models
    $${PWD}/OAIReportCollection.h \
    $${PWD}/OAIReportRecordContract.h \
    $${PWD}/OAIRequestReportCollection.h \
    $${PWD}/OAIRequestReportRecordContract.h \
# APIs
    $${PWD}/OAIReportsApi.h \
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
    $${PWD}/OAIReportCollection.cpp \
    $${PWD}/OAIReportRecordContract.cpp \
    $${PWD}/OAIRequestReportCollection.cpp \
    $${PWD}/OAIRequestReportRecordContract.cpp \
# APIs
    $${PWD}/OAIReportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
