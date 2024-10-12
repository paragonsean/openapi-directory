QT += network

HEADERS += \
# Models
    $${PWD}/OAIReportingPropertyMortgageModel.h \
    $${PWD}/OAIReportingPropertyMortgageModelResults.h \
    $${PWD}/OAIReportingReceivershipCaseDetailsModel.h \
    $${PWD}/OAIReportingReceivershipCaseModel.h \
    $${PWD}/OAIReportingReceivershipCaseModelResults.h \
    $${PWD}/OAIReportingReceivershipExitStrategyModel.h \
    $${PWD}/OAIReportingReceivershipLitigationModel.h \
# APIs
    $${PWD}/OAIReportingControllerApi.h \
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
    $${PWD}/OAIReportingPropertyMortgageModel.cpp \
    $${PWD}/OAIReportingPropertyMortgageModelResults.cpp \
    $${PWD}/OAIReportingReceivershipCaseDetailsModel.cpp \
    $${PWD}/OAIReportingReceivershipCaseModel.cpp \
    $${PWD}/OAIReportingReceivershipCaseModelResults.cpp \
    $${PWD}/OAIReportingReceivershipExitStrategyModel.cpp \
    $${PWD}/OAIReportingReceivershipLitigationModel.cpp \
# APIs
    $${PWD}/OAIReportingControllerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
