QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssessedDisk.h \
    $${PWD}/OAIAssessedMachine.h \
    $${PWD}/OAIAssessedMachineProperties.h \
    $${PWD}/OAIAssessedMachineResultList.h \
    $${PWD}/OAIAssessedNetworkAdapter.h \
    $${PWD}/OAIAssessment.h \
    $${PWD}/OAIAssessmentProperties.h \
    $${PWD}/OAIAssessmentResultList.h \
    $${PWD}/OAIDisk.h \
    $${PWD}/OAIDownloadUrl.h \
    $${PWD}/OAIGroup.h \
    $${PWD}/OAIGroupProperties.h \
    $${PWD}/OAIGroupResultList.h \
    $${PWD}/OAIMachine.h \
    $${PWD}/OAIMachineProperties.h \
    $${PWD}/OAIMachineResultList.h \
    $${PWD}/OAINetworkAdapter.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationResultList.h \
    $${PWD}/OAIProject.h \
    $${PWD}/OAIProjectKey.h \
    $${PWD}/OAIProjectProperties.h \
    $${PWD}/OAIProjectResultList.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAssessedDisk.cpp \
    $${PWD}/OAIAssessedMachine.cpp \
    $${PWD}/OAIAssessedMachineProperties.cpp \
    $${PWD}/OAIAssessedMachineResultList.cpp \
    $${PWD}/OAIAssessedNetworkAdapter.cpp \
    $${PWD}/OAIAssessment.cpp \
    $${PWD}/OAIAssessmentProperties.cpp \
    $${PWD}/OAIAssessmentResultList.cpp \
    $${PWD}/OAIDisk.cpp \
    $${PWD}/OAIDownloadUrl.cpp \
    $${PWD}/OAIGroup.cpp \
    $${PWD}/OAIGroupProperties.cpp \
    $${PWD}/OAIGroupResultList.cpp \
    $${PWD}/OAIMachine.cpp \
    $${PWD}/OAIMachineProperties.cpp \
    $${PWD}/OAIMachineResultList.cpp \
    $${PWD}/OAINetworkAdapter.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationResultList.cpp \
    $${PWD}/OAIProject.cpp \
    $${PWD}/OAIProjectKey.cpp \
    $${PWD}/OAIProjectProperties.cpp \
    $${PWD}/OAIProjectResultList.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
