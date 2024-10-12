QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIBankAccount.h \
    $${PWD}/OAICard.h \
    $${PWD}/OAIDisableRequest.h \
    $${PWD}/OAIDisableResult.h \
    $${PWD}/OAIName.h \
    $${PWD}/OAINotifyShopperRequest.h \
    $${PWD}/OAINotifyShopperResult.h \
    $${PWD}/OAIRecurring.h \
    $${PWD}/OAIRecurringDetail.h \
    $${PWD}/OAIRecurringDetailWrapper.h \
    $${PWD}/OAIRecurringDetailsRequest.h \
    $${PWD}/OAIRecurringDetailsResult.h \
    $${PWD}/OAIScheduleAccountUpdaterRequest.h \
    $${PWD}/OAIScheduleAccountUpdaterResult.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAITokenDetails.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAIBankAccount.cpp \
    $${PWD}/OAICard.cpp \
    $${PWD}/OAIDisableRequest.cpp \
    $${PWD}/OAIDisableResult.cpp \
    $${PWD}/OAIName.cpp \
    $${PWD}/OAINotifyShopperRequest.cpp \
    $${PWD}/OAINotifyShopperResult.cpp \
    $${PWD}/OAIRecurring.cpp \
    $${PWD}/OAIRecurringDetail.cpp \
    $${PWD}/OAIRecurringDetailWrapper.cpp \
    $${PWD}/OAIRecurringDetailsRequest.cpp \
    $${PWD}/OAIRecurringDetailsResult.cpp \
    $${PWD}/OAIScheduleAccountUpdaterRequest.cpp \
    $${PWD}/OAIScheduleAccountUpdaterResult.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAITokenDetails.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
