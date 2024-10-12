/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIMathApi_H
#define OAI_OAIMathApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIInputCalculateMinMax.h"
#include "OAIInputCalculateNumber.h"
#include "OAIInputCalculateNumbers.h"
#include "OAIInputCalculatePower.h"
#include "OAIInputCalculateSeries.h"
#include "OAIInputConvertAngle.h"
#include "OAIInputConvertArea.h"
#include "OAIInputConvertDistance.h"
#include "OAIInputConvertDuration.h"
#include "OAIInputConvertEnergy.h"
#include "OAIInputConvertPower.h"
#include "OAIInputConvertSpeed.h"
#include "OAIInputConvertTemperature.h"
#include "OAIInputConvertVolume.h"
#include "OAIInputConvertWeight.h"
#include "OAIInputNumberRange.h"
#include "OAIOutputNumber.h"
#include "OAIOutputString.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMathApi : public QObject {
    Q_OBJECT

public:
    OAIMathApi(const int timeOut = 0);
    ~OAIMathApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  calculate_number OAIInputCalculateNumber [optional]
    */
    virtual void calculateAbsolute(const ::OpenAPI::OptionalParam<OAIInputCalculateNumber> &calculate_number = ::OpenAPI::OptionalParam<OAIInputCalculateNumber>());

    /**
    * @param[in]  calculate_numbers OAIInputCalculateNumbers [optional]
    */
    virtual void calculateAddition(const ::OpenAPI::OptionalParam<OAIInputCalculateNumbers> &calculate_numbers = ::OpenAPI::OptionalParam<OAIInputCalculateNumbers>());

    /**
    * @param[in]  calculate_series OAIInputCalculateSeries [optional]
    */
    virtual void calculateAverage(const ::OpenAPI::OptionalParam<OAIInputCalculateSeries> &calculate_series = ::OpenAPI::OptionalParam<OAIInputCalculateSeries>());

    /**
    * @param[in]  calculate_number OAIInputCalculateNumber [optional]
    */
    virtual void calculateCosine(const ::OpenAPI::OptionalParam<OAIInputCalculateNumber> &calculate_number = ::OpenAPI::OptionalParam<OAIInputCalculateNumber>());

    /**
    * @param[in]  calculate_numbers OAIInputCalculateNumbers [optional]
    */
    virtual void calculateDivision(const ::OpenAPI::OptionalParam<OAIInputCalculateNumbers> &calculate_numbers = ::OpenAPI::OptionalParam<OAIInputCalculateNumbers>());

    /**
    * @param[in]  calculate_number OAIInputCalculateNumber [optional]
    */
    virtual void calculateLogarithm(const ::OpenAPI::OptionalParam<OAIInputCalculateNumber> &calculate_number = ::OpenAPI::OptionalParam<OAIInputCalculateNumber>());

    /**
    * @param[in]  calculate_series OAIInputCalculateSeries [optional]
    */
    virtual void calculateMedian(const ::OpenAPI::OptionalParam<OAIInputCalculateSeries> &calculate_series = ::OpenAPI::OptionalParam<OAIInputCalculateSeries>());

    /**
    * @param[in]  calculate_series OAIInputCalculateMinMax [optional]
    */
    virtual void calculateMinMax(const ::OpenAPI::OptionalParam<OAIInputCalculateMinMax> &calculate_series = ::OpenAPI::OptionalParam<OAIInputCalculateMinMax>());

    /**
    * @param[in]  calculate_numbers OAIInputCalculateNumbers [optional]
    */
    virtual void calculateModulo(const ::OpenAPI::OptionalParam<OAIInputCalculateNumbers> &calculate_numbers = ::OpenAPI::OptionalParam<OAIInputCalculateNumbers>());

    /**
    * @param[in]  calculate_numbers OAIInputCalculateNumbers [optional]
    */
    virtual void calculateMultiplication(const ::OpenAPI::OptionalParam<OAIInputCalculateNumbers> &calculate_numbers = ::OpenAPI::OptionalParam<OAIInputCalculateNumbers>());

    /**
    * @param[in]  calculate_numbers OAIInputCalculateNumbers [optional]
    */
    virtual void calculateNthRoot(const ::OpenAPI::OptionalParam<OAIInputCalculateNumbers> &calculate_numbers = ::OpenAPI::OptionalParam<OAIInputCalculateNumbers>());

    /**
    * @param[in]  calculate_power OAIInputCalculatePower [optional]
    */
    virtual void calculatePower(const ::OpenAPI::OptionalParam<OAIInputCalculatePower> &calculate_power = ::OpenAPI::OptionalParam<OAIInputCalculatePower>());

    /**
    * @param[in]  calculate_number OAIInputCalculateNumber [optional]
    */
    virtual void calculateSine(const ::OpenAPI::OptionalParam<OAIInputCalculateNumber> &calculate_number = ::OpenAPI::OptionalParam<OAIInputCalculateNumber>());

    /**
    * @param[in]  calculate_number OAIInputCalculateNumber [optional]
    */
    virtual void calculateSquareRoot(const ::OpenAPI::OptionalParam<OAIInputCalculateNumber> &calculate_number = ::OpenAPI::OptionalParam<OAIInputCalculateNumber>());

    /**
    * @param[in]  calculate_numbers OAIInputCalculateNumbers [optional]
    */
    virtual void calculateSubtraction(const ::OpenAPI::OptionalParam<OAIInputCalculateNumbers> &calculate_numbers = ::OpenAPI::OptionalParam<OAIInputCalculateNumbers>());

    /**
    * @param[in]  calculate_series OAIInputCalculateSeries [optional]
    */
    virtual void calculateSum(const ::OpenAPI::OptionalParam<OAIInputCalculateSeries> &calculate_series = ::OpenAPI::OptionalParam<OAIInputCalculateSeries>());

    /**
    * @param[in]  calculate_number OAIInputCalculateNumber [optional]
    */
    virtual void calculateTangent(const ::OpenAPI::OptionalParam<OAIInputCalculateNumber> &calculate_number = ::OpenAPI::OptionalParam<OAIInputCalculateNumber>());

    /**
    * @param[in]  calculate_series OAIInputCalculateSeries [optional]
    */
    virtual void calculateVariance(const ::OpenAPI::OptionalParam<OAIInputCalculateSeries> &calculate_series = ::OpenAPI::OptionalParam<OAIInputCalculateSeries>());

    /**
    * @param[in]  convert_angle OAIInputConvertAngle [optional]
    */
    virtual void convertAngle(const ::OpenAPI::OptionalParam<OAIInputConvertAngle> &convert_angle = ::OpenAPI::OptionalParam<OAIInputConvertAngle>());

    /**
    * @param[in]  convert_area OAIInputConvertArea [optional]
    */
    virtual void convertArea(const ::OpenAPI::OptionalParam<OAIInputConvertArea> &convert_area = ::OpenAPI::OptionalParam<OAIInputConvertArea>());

    /**
    * @param[in]  convert_distance OAIInputConvertDistance [optional]
    */
    virtual void convertDistance(const ::OpenAPI::OptionalParam<OAIInputConvertDistance> &convert_distance = ::OpenAPI::OptionalParam<OAIInputConvertDistance>());

    /**
    * @param[in]  convert_duration OAIInputConvertDuration [optional]
    */
    virtual void convertDuration(const ::OpenAPI::OptionalParam<OAIInputConvertDuration> &convert_duration = ::OpenAPI::OptionalParam<OAIInputConvertDuration>());

    /**
    * @param[in]  convert_energy OAIInputConvertEnergy [optional]
    */
    virtual void convertEnergy(const ::OpenAPI::OptionalParam<OAIInputConvertEnergy> &convert_energy = ::OpenAPI::OptionalParam<OAIInputConvertEnergy>());

    /**
    * @param[in]  convert_power OAIInputConvertPower [optional]
    */
    virtual void convertPower(const ::OpenAPI::OptionalParam<OAIInputConvertPower> &convert_power = ::OpenAPI::OptionalParam<OAIInputConvertPower>());

    /**
    * @param[in]  convert_speed OAIInputConvertSpeed [optional]
    */
    virtual void convertSpeed(const ::OpenAPI::OptionalParam<OAIInputConvertSpeed> &convert_speed = ::OpenAPI::OptionalParam<OAIInputConvertSpeed>());

    /**
    * @param[in]  convert_temperature OAIInputConvertTemperature [optional]
    */
    virtual void convertTemperature(const ::OpenAPI::OptionalParam<OAIInputConvertTemperature> &convert_temperature = ::OpenAPI::OptionalParam<OAIInputConvertTemperature>());

    /**
    * @param[in]  convert_volume OAIInputConvertVolume [optional]
    */
    virtual void convertVolume(const ::OpenAPI::OptionalParam<OAIInputConvertVolume> &convert_volume = ::OpenAPI::OptionalParam<OAIInputConvertVolume>());

    /**
    * @param[in]  convert_weight OAIInputConvertWeight [optional]
    */
    virtual void convertWeight(const ::OpenAPI::OptionalParam<OAIInputConvertWeight> &convert_weight = ::OpenAPI::OptionalParam<OAIInputConvertWeight>());

    /**
    * @param[in]  number_range OAIInputNumberRange [optional]
    */
    virtual void randomNumber(const ::OpenAPI::OptionalParam<OAIInputNumberRange> &number_range = ::OpenAPI::OptionalParam<OAIInputNumberRange>());

    /**
    * @param[in]  calculate_number OAIInputCalculateNumber [optional]
    */
    virtual void roundNumber(const ::OpenAPI::OptionalParam<OAIInputCalculateNumber> &calculate_number = ::OpenAPI::OptionalParam<OAIInputCalculateNumber>());

    /**
    * @param[in]  calculate_series OAIInputCalculateSeries [optional]
    */
    virtual void standardDeviation(const ::OpenAPI::OptionalParam<OAIInputCalculateSeries> &calculate_series = ::OpenAPI::OptionalParam<OAIInputCalculateSeries>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void calculateAbsoluteCallback(OAIHttpRequestWorker *worker);
    void calculateAdditionCallback(OAIHttpRequestWorker *worker);
    void calculateAverageCallback(OAIHttpRequestWorker *worker);
    void calculateCosineCallback(OAIHttpRequestWorker *worker);
    void calculateDivisionCallback(OAIHttpRequestWorker *worker);
    void calculateLogarithmCallback(OAIHttpRequestWorker *worker);
    void calculateMedianCallback(OAIHttpRequestWorker *worker);
    void calculateMinMaxCallback(OAIHttpRequestWorker *worker);
    void calculateModuloCallback(OAIHttpRequestWorker *worker);
    void calculateMultiplicationCallback(OAIHttpRequestWorker *worker);
    void calculateNthRootCallback(OAIHttpRequestWorker *worker);
    void calculatePowerCallback(OAIHttpRequestWorker *worker);
    void calculateSineCallback(OAIHttpRequestWorker *worker);
    void calculateSquareRootCallback(OAIHttpRequestWorker *worker);
    void calculateSubtractionCallback(OAIHttpRequestWorker *worker);
    void calculateSumCallback(OAIHttpRequestWorker *worker);
    void calculateTangentCallback(OAIHttpRequestWorker *worker);
    void calculateVarianceCallback(OAIHttpRequestWorker *worker);
    void convertAngleCallback(OAIHttpRequestWorker *worker);
    void convertAreaCallback(OAIHttpRequestWorker *worker);
    void convertDistanceCallback(OAIHttpRequestWorker *worker);
    void convertDurationCallback(OAIHttpRequestWorker *worker);
    void convertEnergyCallback(OAIHttpRequestWorker *worker);
    void convertPowerCallback(OAIHttpRequestWorker *worker);
    void convertSpeedCallback(OAIHttpRequestWorker *worker);
    void convertTemperatureCallback(OAIHttpRequestWorker *worker);
    void convertVolumeCallback(OAIHttpRequestWorker *worker);
    void convertWeightCallback(OAIHttpRequestWorker *worker);
    void randomNumberCallback(OAIHttpRequestWorker *worker);
    void roundNumberCallback(OAIHttpRequestWorker *worker);
    void standardDeviationCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void calculateAbsoluteSignal(OAIOutputNumber summary);
    void calculateAdditionSignal(OAIOutputNumber summary);
    void calculateAverageSignal(OAIOutputNumber summary);
    void calculateCosineSignal(OAIOutputNumber summary);
    void calculateDivisionSignal(OAIOutputNumber summary);
    void calculateLogarithmSignal(OAIOutputNumber summary);
    void calculateMedianSignal(OAIOutputNumber summary);
    void calculateMinMaxSignal(OAIOutputNumber summary);
    void calculateModuloSignal(OAIOutputNumber summary);
    void calculateMultiplicationSignal(OAIOutputNumber summary);
    void calculateNthRootSignal(OAIOutputNumber summary);
    void calculatePowerSignal(OAIOutputNumber summary);
    void calculateSineSignal(OAIOutputNumber summary);
    void calculateSquareRootSignal(OAIOutputNumber summary);
    void calculateSubtractionSignal(OAIOutputNumber summary);
    void calculateSumSignal(OAIOutputNumber summary);
    void calculateTangentSignal(OAIOutputNumber summary);
    void calculateVarianceSignal(OAIOutputNumber summary);
    void convertAngleSignal(OAIOutputNumber summary);
    void convertAreaSignal(OAIOutputNumber summary);
    void convertDistanceSignal(OAIOutputNumber summary);
    void convertDurationSignal(OAIOutputNumber summary);
    void convertEnergySignal(OAIOutputNumber summary);
    void convertPowerSignal(OAIOutputNumber summary);
    void convertSpeedSignal(OAIOutputNumber summary);
    void convertTemperatureSignal(OAIOutputNumber summary);
    void convertVolumeSignal(OAIOutputNumber summary);
    void convertWeightSignal(OAIOutputNumber summary);
    void randomNumberSignal(OAIOutputNumber summary);
    void roundNumberSignal(OAIOutputNumber summary);
    void standardDeviationSignal(OAIOutputNumber summary);


    void calculateAbsoluteSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateAdditionSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateAverageSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateCosineSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateDivisionSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateLogarithmSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateMedianSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateMinMaxSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateModuloSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateMultiplicationSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateNthRootSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculatePowerSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateSineSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateSquareRootSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateSubtractionSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateSumSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateTangentSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void calculateVarianceSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertAngleSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertAreaSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertDistanceSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertDurationSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertEnergySignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertPowerSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertSpeedSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertTemperatureSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertVolumeSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void convertWeightSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void randomNumberSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void roundNumberSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);
    void standardDeviationSignalFull(OAIHttpRequestWorker *worker, OAIOutputNumber summary);

    Q_DECL_DEPRECATED_X("Use calculateAbsoluteSignalError() instead")
    void calculateAbsoluteSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateAbsoluteSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateAdditionSignalError() instead")
    void calculateAdditionSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateAdditionSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateAverageSignalError() instead")
    void calculateAverageSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateAverageSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateCosineSignalError() instead")
    void calculateCosineSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateCosineSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateDivisionSignalError() instead")
    void calculateDivisionSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateDivisionSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateLogarithmSignalError() instead")
    void calculateLogarithmSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateLogarithmSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateMedianSignalError() instead")
    void calculateMedianSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateMedianSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateMinMaxSignalError() instead")
    void calculateMinMaxSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateMinMaxSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateModuloSignalError() instead")
    void calculateModuloSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateModuloSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateMultiplicationSignalError() instead")
    void calculateMultiplicationSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateMultiplicationSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateNthRootSignalError() instead")
    void calculateNthRootSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateNthRootSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculatePowerSignalError() instead")
    void calculatePowerSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculatePowerSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSineSignalError() instead")
    void calculateSineSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSineSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSquareRootSignalError() instead")
    void calculateSquareRootSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSquareRootSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSubtractionSignalError() instead")
    void calculateSubtractionSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSubtractionSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSumSignalError() instead")
    void calculateSumSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSumSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateTangentSignalError() instead")
    void calculateTangentSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateTangentSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateVarianceSignalError() instead")
    void calculateVarianceSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateVarianceSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertAngleSignalError() instead")
    void convertAngleSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertAngleSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertAreaSignalError() instead")
    void convertAreaSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertAreaSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertDistanceSignalError() instead")
    void convertDistanceSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertDistanceSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertDurationSignalError() instead")
    void convertDurationSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertDurationSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertEnergySignalError() instead")
    void convertEnergySignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertEnergySignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertPowerSignalError() instead")
    void convertPowerSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertPowerSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertSpeedSignalError() instead")
    void convertSpeedSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertSpeedSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertTemperatureSignalError() instead")
    void convertTemperatureSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertTemperatureSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertVolumeSignalError() instead")
    void convertVolumeSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertVolumeSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertWeightSignalError() instead")
    void convertWeightSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void convertWeightSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use randomNumberSignalError() instead")
    void randomNumberSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void randomNumberSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use roundNumberSignalError() instead")
    void roundNumberSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void roundNumberSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use standardDeviationSignalError() instead")
    void standardDeviationSignalE(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, QString error_str);
    void standardDeviationSignalError(OAIOutputNumber summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use calculateAbsoluteSignalErrorFull() instead")
    void calculateAbsoluteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateAbsoluteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateAdditionSignalErrorFull() instead")
    void calculateAdditionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateAdditionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateAverageSignalErrorFull() instead")
    void calculateAverageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateAverageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateCosineSignalErrorFull() instead")
    void calculateCosineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateCosineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateDivisionSignalErrorFull() instead")
    void calculateDivisionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateDivisionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateLogarithmSignalErrorFull() instead")
    void calculateLogarithmSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateLogarithmSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateMedianSignalErrorFull() instead")
    void calculateMedianSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateMedianSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateMinMaxSignalErrorFull() instead")
    void calculateMinMaxSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateMinMaxSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateModuloSignalErrorFull() instead")
    void calculateModuloSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateModuloSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateMultiplicationSignalErrorFull() instead")
    void calculateMultiplicationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateMultiplicationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateNthRootSignalErrorFull() instead")
    void calculateNthRootSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateNthRootSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculatePowerSignalErrorFull() instead")
    void calculatePowerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculatePowerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSineSignalErrorFull() instead")
    void calculateSineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSquareRootSignalErrorFull() instead")
    void calculateSquareRootSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSquareRootSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSubtractionSignalErrorFull() instead")
    void calculateSubtractionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSubtractionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateSumSignalErrorFull() instead")
    void calculateSumSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSumSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateTangentSignalErrorFull() instead")
    void calculateTangentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateTangentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateVarianceSignalErrorFull() instead")
    void calculateVarianceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateVarianceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertAngleSignalErrorFull() instead")
    void convertAngleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertAngleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertAreaSignalErrorFull() instead")
    void convertAreaSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertAreaSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertDistanceSignalErrorFull() instead")
    void convertDistanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertDistanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertDurationSignalErrorFull() instead")
    void convertDurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertDurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertEnergySignalErrorFull() instead")
    void convertEnergySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertEnergySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertPowerSignalErrorFull() instead")
    void convertPowerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertPowerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertSpeedSignalErrorFull() instead")
    void convertSpeedSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertSpeedSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertTemperatureSignalErrorFull() instead")
    void convertTemperatureSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertTemperatureSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertVolumeSignalErrorFull() instead")
    void convertVolumeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertVolumeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use convertWeightSignalErrorFull() instead")
    void convertWeightSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void convertWeightSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use randomNumberSignalErrorFull() instead")
    void randomNumberSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void randomNumberSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use roundNumberSignalErrorFull() instead")
    void roundNumberSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void roundNumberSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use standardDeviationSignalErrorFull() instead")
    void standardDeviationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void standardDeviationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
