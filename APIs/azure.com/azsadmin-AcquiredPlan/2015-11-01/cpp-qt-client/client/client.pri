QT += network

HEADERS += \
# Models
    $${PWD}/OAIPlanAcquisition.h \
    $${PWD}/OAIPlanAcquisitionList.h \
    $${PWD}/OAIProvisioningState.h \
# APIs
    $${PWD}/OAIAcquiredPlansApi.h \
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
    $${PWD}/OAIPlanAcquisition.cpp \
    $${PWD}/OAIPlanAcquisitionList.cpp \
    $${PWD}/OAIProvisioningState.cpp \
# APIs
    $${PWD}/OAIAcquiredPlansApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
