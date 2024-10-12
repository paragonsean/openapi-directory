QT += network

HEADERS += \
# Models
    $${PWD}/OAIElasticPoolActivity.h \
    $${PWD}/OAIElasticPoolActivityListResult.h \
    $${PWD}/OAIElasticPoolActivityProperties.h \
    $${PWD}/OAIElasticPoolDatabaseActivity.h \
    $${PWD}/OAIElasticPoolDatabaseActivityListResult.h \
    $${PWD}/OAIElasticPoolDatabaseActivityProperties.h \
    $${PWD}/OAIOperationImpact.h \
    $${PWD}/OAIRecommendedIndex.h \
    $${PWD}/OAIRecommendedIndexProperties.h \
    $${PWD}/OAIServiceTierAdvisor.h \
    $${PWD}/OAIServiceTierAdvisorListResult.h \
    $${PWD}/OAIServiceTierAdvisorProperties.h \
    $${PWD}/OAISloUsageMetric.h \
    $${PWD}/OAITransparentDataEncryption.h \
    $${PWD}/OAITransparentDataEncryptionActivity.h \
    $${PWD}/OAITransparentDataEncryptionActivityListResult.h \
    $${PWD}/OAITransparentDataEncryptionActivityProperties.h \
    $${PWD}/OAITransparentDataEncryptionProperties.h \
# APIs
    $${PWD}/OAIElasticPoolsApi.h \
    $${PWD}/OAIServiceTierAdvisorsApi.h \
    $${PWD}/OAITransparentDataEncryptionApi.h \
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
    $${PWD}/OAIElasticPoolActivity.cpp \
    $${PWD}/OAIElasticPoolActivityListResult.cpp \
    $${PWD}/OAIElasticPoolActivityProperties.cpp \
    $${PWD}/OAIElasticPoolDatabaseActivity.cpp \
    $${PWD}/OAIElasticPoolDatabaseActivityListResult.cpp \
    $${PWD}/OAIElasticPoolDatabaseActivityProperties.cpp \
    $${PWD}/OAIOperationImpact.cpp \
    $${PWD}/OAIRecommendedIndex.cpp \
    $${PWD}/OAIRecommendedIndexProperties.cpp \
    $${PWD}/OAIServiceTierAdvisor.cpp \
    $${PWD}/OAIServiceTierAdvisorListResult.cpp \
    $${PWD}/OAIServiceTierAdvisorProperties.cpp \
    $${PWD}/OAISloUsageMetric.cpp \
    $${PWD}/OAITransparentDataEncryption.cpp \
    $${PWD}/OAITransparentDataEncryptionActivity.cpp \
    $${PWD}/OAITransparentDataEncryptionActivityListResult.cpp \
    $${PWD}/OAITransparentDataEncryptionActivityProperties.cpp \
    $${PWD}/OAITransparentDataEncryptionProperties.cpp \
# APIs
    $${PWD}/OAIElasticPoolsApi.cpp \
    $${PWD}/OAIServiceTierAdvisorsApi.cpp \
    $${PWD}/OAITransparentDataEncryptionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
