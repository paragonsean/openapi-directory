QT += network

HEADERS += \
# Models
    $${PWD}/OAIMaintenanceDocumentModel.h \
    $${PWD}/OAIMaintenanceIssueModel.h \
# APIs
    $${PWD}/OAIMaintenanceControllerApi.h \
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
    $${PWD}/OAIMaintenanceDocumentModel.cpp \
    $${PWD}/OAIMaintenanceIssueModel.cpp \
# APIs
    $${PWD}/OAIMaintenanceControllerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
