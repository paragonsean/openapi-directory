QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccounts.h \
    $${PWD}/OAICards.h \
    $${PWD}/OAIContracts.h \
    $${PWD}/OAIEntities.h \
    $${PWD}/OAIEntity_data.h \
    $${PWD}/OAIEntity_data_anyOf.h \
    $${PWD}/OAIEntity_data_anyOf_1.h \
    $${PWD}/OAIEntity_data_anyOf_2.h \
    $${PWD}/OAIEntity_data_anyOf_3.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_codes.h \
    $${PWD}/OAIError_detail.h \
    $${PWD}/OAIOwner.h \
    $${PWD}/OAIPortfolios.h \
    $${PWD}/OAIProperties.h \
    $${PWD}/OAIProperties_historic_prices_inner.h \
    $${PWD}/OAIStatistics.h \
    $${PWD}/OAIUser_information.h \
# APIs
    $${PWD}/OAIEntityDataApi.h \
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
    $${PWD}/OAIAccounts.cpp \
    $${PWD}/OAICards.cpp \
    $${PWD}/OAIContracts.cpp \
    $${PWD}/OAIEntities.cpp \
    $${PWD}/OAIEntity_data.cpp \
    $${PWD}/OAIEntity_data_anyOf.cpp \
    $${PWD}/OAIEntity_data_anyOf_1.cpp \
    $${PWD}/OAIEntity_data_anyOf_2.cpp \
    $${PWD}/OAIEntity_data_anyOf_3.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_codes.cpp \
    $${PWD}/OAIError_detail.cpp \
    $${PWD}/OAIOwner.cpp \
    $${PWD}/OAIPortfolios.cpp \
    $${PWD}/OAIProperties.cpp \
    $${PWD}/OAIProperties_historic_prices_inner.cpp \
    $${PWD}/OAIStatistics.cpp \
    $${PWD}/OAIUser_information.cpp \
# APIs
    $${PWD}/OAIEntityDataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
