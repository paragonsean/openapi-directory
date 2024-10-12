QT += network

HEADERS += \
# Models
    $${PWD}/OAILicenseAssignment.h \
    $${PWD}/OAILicenseAssignmentInsert.h \
    $${PWD}/OAILicenseAssignmentList.h \
# APIs
    $${PWD}/OAILicenseAssignmentsApi.h \
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
    $${PWD}/OAILicenseAssignment.cpp \
    $${PWD}/OAILicenseAssignmentInsert.cpp \
    $${PWD}/OAILicenseAssignmentList.cpp \
# APIs
    $${PWD}/OAILicenseAssignmentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
