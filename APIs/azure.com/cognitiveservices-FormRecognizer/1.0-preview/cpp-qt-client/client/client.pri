QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnalyzeResult.h \
    $${PWD}/OAIAnalyzeWithCustomModel_request.h \
    $${PWD}/OAIErrorInformation.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIExtractedKeyValuePair.h \
    $${PWD}/OAIExtractedPage.h \
    $${PWD}/OAIExtractedTable.h \
    $${PWD}/OAIExtractedTableColumn.h \
    $${PWD}/OAIExtractedToken.h \
    $${PWD}/OAIFormDocumentReport.h \
    $${PWD}/OAIFormOperationError.h \
    $${PWD}/OAIInnerError.h \
    $${PWD}/OAIKeysResult.h \
    $${PWD}/OAIModelResult.h \
    $${PWD}/OAIModelsResult.h \
    $${PWD}/OAITrainRequest.h \
    $${PWD}/OAITrainResult.h \
    $${PWD}/OAITrainSourceFilter.h \
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
    $${PWD}/OAIAnalyzeResult.cpp \
    $${PWD}/OAIAnalyzeWithCustomModel_request.cpp \
    $${PWD}/OAIErrorInformation.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIExtractedKeyValuePair.cpp \
    $${PWD}/OAIExtractedPage.cpp \
    $${PWD}/OAIExtractedTable.cpp \
    $${PWD}/OAIExtractedTableColumn.cpp \
    $${PWD}/OAIExtractedToken.cpp \
    $${PWD}/OAIFormDocumentReport.cpp \
    $${PWD}/OAIFormOperationError.cpp \
    $${PWD}/OAIInnerError.cpp \
    $${PWD}/OAIKeysResult.cpp \
    $${PWD}/OAIModelResult.cpp \
    $${PWD}/OAIModelsResult.cpp \
    $${PWD}/OAITrainRequest.cpp \
    $${PWD}/OAITrainResult.cpp \
    $${PWD}/OAITrainSourceFilter.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
