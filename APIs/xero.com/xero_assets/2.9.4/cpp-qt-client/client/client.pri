QT += network

HEADERS += \
# Models
    $${PWD}/OAIAsset.h \
    $${PWD}/OAIAssetStatus.h \
    $${PWD}/OAIAssetStatusQueryParam.h \
    $${PWD}/OAIAssetType.h \
    $${PWD}/OAIAssets.h \
    $${PWD}/OAIBookDepreciationDetail.h \
    $${PWD}/OAIBookDepreciationSetting.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIFieldValidationErrorsElement.h \
    $${PWD}/OAIPagination.h \
    $${PWD}/OAIResourceValidationErrorsElement.h \
    $${PWD}/OAISetting.h \
# APIs
    $${PWD}/OAIAssetApi.h \
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
    $${PWD}/OAIAsset.cpp \
    $${PWD}/OAIAssetStatus.cpp \
    $${PWD}/OAIAssetStatusQueryParam.cpp \
    $${PWD}/OAIAssetType.cpp \
    $${PWD}/OAIAssets.cpp \
    $${PWD}/OAIBookDepreciationDetail.cpp \
    $${PWD}/OAIBookDepreciationSetting.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIFieldValidationErrorsElement.cpp \
    $${PWD}/OAIPagination.cpp \
    $${PWD}/OAIResourceValidationErrorsElement.cpp \
    $${PWD}/OAISetting.cpp \
# APIs
    $${PWD}/OAIAssetApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
