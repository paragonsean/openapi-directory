/**
 * Taxrates.io API
 * <h3>Introduction</h3> <p>Taxrates.io is a global tax rate service that automates the management of monitoring tax rates changes in 181 countries. We monitor over 14,000 US sales tax, VAT, GST rates for you and make updates via our API so you always have the most update tax rates.</p> <p>You can use Taxrates.io as a virtual sandbox where we provide you with 30 days free trial.</p> <h3>Countries</h3> <p>We currently support the following countries around the world. If you would like to request the addition of a new country, please email us at <a href=\"mailto:support@taxrates.io\">support@taxrates.io</a></p> <table>   <tr><td>Afghanistan</td><td>Gambia</td><td>Nicaragua</td></tr>   <tr><td>Albania</td><td>Georgia</td><td>Niger</td></tr>   <tr><td>Andorra</td><td>Germany</td><td>Nigeria</td></tr>   <tr><td>Angola</td><td>Ghana</td><td>North Korea</td></tr>   <tr><td>Antigua and Barbuda</td><td>Greece</td><td>Norway</td></tr>   <tr><td>Argentina</td><td>Grenada</td><td>Pakistan</td></tr>   <tr><td>Armenia</td><td>Guam</td><td>Palestine</td></tr>   <tr><td>Aruba</td><td>Guatemala</td><td>Panama</td></tr>   <tr><td>Australia</td><td>Guinea</td><td>Papua New Guinea</td></tr>   <tr><td>Austria</td><td>Guyana</td><td>Paraguay</td></tr>   <tr><td>Azerbaijan</td><td>Haiti</td><td>Peru</td></tr>   <tr><td>Bahamas</td><td>Honduras</td><td>Philippines</td></tr>   <tr><td>Bangladesh</td><td>Hungary</td><td>Poland</td></tr>   <tr><td>Barbados</td><td>Iceland</td><td>Portugal</td></tr>   <tr><td>Belarus</td><td>India</td><td>Puerto Rico</td></tr>   <tr><td>Belgium</td><td>Indonesia</td><td>Republic of the Congo</td></tr>   <tr><td>Belize</td><td>Iran</td><td>Romania</td></tr>   <tr><td>Benin</td><td>Ireland</td><td>Russian Federation</td></tr>   <tr><td>Bhutan</td><td>Isle of Man</td><td>Rwanda</td></tr>   <tr><td>Bolivia</td><td>Israel</td><td>Samoa</td></tr>   <tr><td>Bonaire</td><td>Italy</td><td>Senegal</td></tr>   <tr><td>Bosnia and Herzegovina</td><td>Japan</td><td>Serbia</td></tr>   <tr><td>Botswana</td><td>Jersey</td><td>Seychelles</td></tr>   <tr><td>Brazil</td><td>Jordan</td><td>Sierra Leone</td></tr>   <tr><td>Bulgaria</td><td>Jordan</td><td>Singapore</td></tr>   <tr><td>Burkina Faso</td><td>Kazakhstan</td><td>Slovakia</td></tr>   <tr><td>Burundi</td><td>Kenya</td><td>Slovenia</td></tr>   <tr><td>Cambodia</td><td>Kiribati</td><td>Solomon Islands</td></tr>   <tr><td>Cameroon</td><td>Kosovo</td><td>Somalia</td></tr>   <tr><td>Cape Verde</td><td>Kyrgyzstan</td><td>South Africa</td></tr>   <tr><td>Central African Republic</td><td>Laos</td><td>South Korea</td></tr>   <tr><td>Chad</td><td>Latvia</td><td>South Sudan</td></tr>   <tr><td>Chile</td><td>Lebanon</td><td>Spain</td></tr>   <tr><td>China</td><td>Lesotho</td><td>Sri Lanka</td></tr>   <tr><td>Columbia</td><td>Liberia</td><td>St Lucia</td></tr>   <tr><td>Comoros</td><td>Liechtenstein</td><td>Sudan</td></tr>   <tr><td>Cook Islands</td><td>Lithuania</td><td>Suriname</td></tr>   <tr><td>Costa Rica</td><td>Luxembourg</td><td>Swaziland</td></tr>   <tr><td>Cote d'Ivoire</td><td>Macedonia</td><td>Sweden</td></tr>   <tr><td>Croatia</td><td>Madagascar</td><td>Switzerland</td></tr>   <tr><td>Cuba</td><td>Malawi</td><td>Tahiti</td></tr>   <tr><td>Curacao</td><td>Malaysia</td><td>Taiwan</td></tr>   <tr><td>Cyprus</td><td>Maldives</td><td>Tajikistan</td></tr>   <tr><td>Czech Republic</td><td>Mali</td><td>Tanzania</td></tr>   <tr><td>Democratic Republic of the Congo</td><td>Malta</td><td>Thailand</td></tr>   <tr><td>Denmark</td><td>Mauritania</td><td>Togo</td></tr>   <tr><td>Djbouti</td><td>Mauritius</td><td>Tonga</td></tr>   <tr><td>Dominica</td><td>Mexico</td><td>Trinidad and Tobago</td></tr>   <tr><td>Dominican Republic</td><td>Micronesia</td><td>Tunisia</td></tr>   <tr><td>Ecuador</td><td>Moldova</td><td>Turkmenistan</td></tr>   <tr><td>Egypt</td><td>Monaco</td><td>Tuvalu</td></tr>   <tr><td>El Salvador</td><td>Mongolia</td><td>Uganda</td></tr>   <tr><td>Equatorial Guinea</td><td>Montenegro</td><td>Ukraine</td></tr>   <tr><td>Eritrea</td><td>Morocco</td><td>United Kingdom</td></tr>   <tr><td>Estonia</td><td>Mozambique</td><td>United States</td></tr>   <tr><td>Ethiopia</td><td>Myanmar</td><td>Uruguay</td></tr>   <tr><td>Fiji</td><td>Namibia</td><td>Vanuatu</td></tr>   <tr><td>Finland</td><td>Nepal</td><td>Venezuela</td></tr>   <tr><td>France</td><td>Netherlands</td><td>Vietnam</td></tr>   <tr><td>Gabon</td><td>New Zealand</td><td>Yemen</td></tr> </table> <h3>Products codes</h3> <p>The Taxrates.io API’s provides product-level tax rates for a subset of product codes. These codes are to be used for products that are either exempt from tax in some jurisdictions or are taxed at reduced rates.</p> <p>We will be expanding support for additional, less common categories over time. If you would like to request the addition of a new product category, please email us at <a href=\"mailto:support@taxrates.io\">support@taxrates.io</a></p> <p>Please select a product code/s when making a request to the Taxrates.io API</p> <table>   <tr><th>Product code</th><th>Product Description</th></tr>   <tr><td>C010</td><td>Services which are not subject to a service-specific tax</td></tr>   <tr><td>C011</td><td>Software - Downloaded</td></tr>   <tr><td>C012</td><td>Books - Downloaded</td></tr>   <tr><td>C011</td><td>Music - Downloaded</td></tr>   <tr><td>C011</td><td>Movies/Digital Video - Downloaded</td></tr>   <tr><td>C011</td><td>Other Electronic Goods - Downloaded</td></tr>   <tr><td>C011</td><td>Streaming Music/Audio Services new</td></tr>   <tr><td>C011</td><td>Streaming Video Services new</td></tr>   <tr><td>C018</td><td>Software as a Services, Generally (Remote Access to Hosted Software)</td></tr>   <tr><td>C018</td><td>Remote Access to Hosted Software - Personal Use</td></tr>   <tr><td>C018</td><td>Remote Access to Hosted Software - Business Use</td></tr>   <tr><td>C021</td><td>Remote Access to Hosted Business Custom Applications</td></tr>   <tr><td>C021</td><td>Personal Cloud Storage/Backup</td></tr>   <tr><td>C021</td><td>Business Cloud Storage/Backup</td></tr>   <tr><td>C021</td><td>Business Data Warehouses</td></tr>   <tr><td>C022</td><td>Infrastructure as Service, Generally</td></tr>   <tr><td>C022</td><td>Ecommerce Site/Webserver Hosting</td></tr>   <tr><td>C022</td><td>Provision of Virtual Computing Capacity</td></tr>   <tr><td>C022</td><td>Software - package or canned program</td></tr>   <tr><td>C022</td><td>Software - modifications to canned program</td></tr>   <tr><td>C022</td><td>Software - custom programs - material</td></tr>   <tr><td>C022</td><td>Software - custom programs - professional serv.</td></tr>   <tr><td>C022</td><td>Information services</td></tr>   <tr><td>C022</td><td>Data processing services</td></tr>   <tr><td>C022</td><td>Mainframe computer access and processing serv.</td></tr>   <tr><td>C022</td><td>Online Data processing services</td></tr> </table> <h3>Filtering</h3> <p>When calling the API endpoints you can use 'filter' parameters to get tax rate for the selected type. You can get the following tax types (Each tax rate will always have one of following types)</p> <h3>US Sales tax Rates</h3> <ol>   <li>CombinedRate</li>   <li>StateRate</li>   <li>CountyRate</li>   <li>CityRate</li>   <li>SpecialRate</li> </ol> <p>We recommend using <a href=\"https://www.getpostman.com/\">Postman</a> when discovering our API. Happy using!</p> <h3>Rate Limiting</h3> <p>We limit API requests.</p> <p>If you’re exceeding this rate and encountering 429 errors, review the following:</p> <ul>   <li>Only make requests in states / regions where you have enabled.</li>   <li>Cache responses if the order details haven’t changed since the last calculation at checkout.</li> </ul> <h3>Errors</h3> <p>The Taxrates.io API uses the following error codes:<p/> <table>   <tr><th>Code</th><th>Error Message</th></tr>   <tr><td>400</td><td>Bad Request – Your request format is bad.</td></tr>   <tr><td>401</td><td>Unauthorized – Your API key is wrong.</td></tr>   <tr><td>404</td><td>Not Found – The specified resource could not be found.</td></tr>   <tr><td>405</td><td>Method Not Allowed – You tried to access a resource with an invalid method.</td></tr>   <tr><td>429</td><td>Too Many Requests – You’re requesting too many resources! Slow down!</td></tr>   <tr><td>500</td><td>Internal Server Error – We had a problem with our server. Try again later.</td></tr>   <tr><td>503</td><td>Service Unavailable – We’re temporarily offline for maintenance. Try again later.</td></tr> </table> <p>Verify your API token is correct and make sure you’re correctly setting the <a href=\"#authentication\">Authorization header</a>.</p> <p>If you’re still not sure what’s wrong, <a href=\"mailto:support@taxrates.io\">contact us</a> and we’ll investigate.</p> <h3>Changelog</h3> <p>Stay on top of new developer-facing features, accuracy improvements, and bug fixes for our API. Have a request? Encounter an issue? <a href=\"mailto:support@taxrates.io\">We’d love to hear your feedback.</a></p>   Contact Support:  Name: apiteam@taxrates.io
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include <QDebug>
#include <QJsonParseError>
#include "OAIHelpers.h"

namespace OpenAPI {

class OAISerializerSettings {
public:
    struct CustomDateTimeFormat{
        bool isStringSet = false;
        QString formatString;
        bool isEnumSet = false;
        Qt::DateFormat formatEnum;
    };

    static CustomDateTimeFormat getCustomDateTimeFormat() {
        return getInstance()->customDateTimeFormat;
    }

    static void setDateTimeFormatString(const QString &dtFormat){
        getInstance()->customDateTimeFormat.isStringSet = true;
        getInstance()->customDateTimeFormat.isEnumSet = false;
        getInstance()->customDateTimeFormat.formatString = dtFormat;
    }

    static void setDateTimeFormatEnum(const Qt::DateFormat &dtFormat){
        getInstance()->customDateTimeFormat.isEnumSet = true;
        getInstance()->customDateTimeFormat.isStringSet = false;
        getInstance()->customDateTimeFormat.formatEnum = dtFormat;
    }

    static OAISerializerSettings *getInstance(){
        if(instance == nullptr){
            instance = new OAISerializerSettings();
        }
        return instance;
    }

private:
    explicit OAISerializerSettings(){
        instance = this;
        customDateTimeFormat.isStringSet = false;
        customDateTimeFormat.isEnumSet = false;
    }
    static OAISerializerSettings *instance;
    CustomDateTimeFormat customDateTimeFormat;
};

OAISerializerSettings * OAISerializerSettings::instance = nullptr;

bool setDateTimeFormat(const QString &dateTimeFormat){
    bool success = false;
    auto dt = QDateTime::fromString(QDateTime::currentDateTime().toString(dateTimeFormat), dateTimeFormat);
    if (dt.isValid()) {
        success = true;
        OAISerializerSettings::setDateTimeFormatString(dateTimeFormat);
    }
    return success;
}

bool setDateTimeFormat(const Qt::DateFormat &dateTimeFormat){
    bool success = false;
    auto dt = QDateTime::fromString(QDateTime::currentDateTime().toString(dateTimeFormat), dateTimeFormat);
    if (dt.isValid()) {
        success = true;
        OAISerializerSettings::setDateTimeFormatEnum(dateTimeFormat);
    }
    return success;
}

QString toStringValue(const QString &value) {
    return value;
}

QString toStringValue(const QDateTime &value) {
    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
        return value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
    }

    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
        return value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
    }

    // ISO 8601
    return value.toString(Qt::ISODate);
}

QString toStringValue(const QByteArray &value) {
    return QString(value);
}

QString toStringValue(const QDate &value) {
    // ISO 8601
    return value.toString(Qt::DateFormat::ISODate);
}

QString toStringValue(const qint32 &value) {
    return QString::number(value);
}

QString toStringValue(const qint64 &value) {
    return QString::number(value);
}

QString toStringValue(const bool &value) {
    return QString(value ? "true" : "false");
}

QString toStringValue(const float &value) {
    return QString::number(static_cast<double>(value));
}

QString toStringValue(const double &value) {
    return QString::number(value);
}

QString toStringValue(const OAIObject &value) {
    return value.asJson();
}

QString toStringValue(const OAIEnum &value) {
    return value.asJson();
}

QString toStringValue(const OAIHttpFileElement &value) {
    return value.asJson();
}

QJsonValue toJsonValue(const QString &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const QDateTime &value) {
    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
        return QJsonValue(value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString));
    }

    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
        return QJsonValue(value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum));
    }

    // ISO 8601
    return QJsonValue(value.toString(Qt::ISODate));
}

QJsonValue toJsonValue(const QByteArray &value) {
    return QJsonValue(QString(value.toBase64()));
}

QJsonValue toJsonValue(const QDate &value) {
    return QJsonValue(value.toString(Qt::ISODate));
}

QJsonValue toJsonValue(const qint32 &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const qint64 &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const bool &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const float &value) {
    return QJsonValue(static_cast<double>(value));
}

QJsonValue toJsonValue(const double &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const OAIObject &value) {
    return value.asJsonObject();
}

QJsonValue toJsonValue(const OAIEnum &value) {
    return value.asJsonValue();
}

QJsonValue toJsonValue(const OAIHttpFileElement &value) {
    return value.asJsonValue();
}

QJsonValue toJsonValue(const QJsonValue &value) {
    return value;
}

bool fromStringValue(const QString &inStr, QString &value) {
    value.clear();
    value.append(inStr);
    return !inStr.isEmpty();
}

bool fromStringValue(const QString &inStr, QDateTime &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
       QDateTime dateTime;
        if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
            dateTime = QDateTime::fromString(inStr, OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
        } else if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
            dateTime = QDateTime::fromString(inStr, OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
        } else {
            dateTime = QDateTime::fromString(inStr, Qt::ISODate);
        }

        if (dateTime.isValid()) {
            value.setDate(dateTime.date());
            value.setTime(dateTime.time());
        } else {
            qDebug() << "DateTime is invalid";
        }
        return dateTime.isValid();
    }
}

bool fromStringValue(const QString &inStr, QByteArray &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
        value.clear();
        value.append(inStr.toUtf8());
        return !value.isEmpty();
    }
}

bool fromStringValue(const QString &inStr, QDate &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
        auto date = QDate::fromString(inStr, Qt::DateFormat::ISODate);
        if (date.isValid()) {
            value.setDate(date.year(), date.month(), date.day());
        } else {
            qDebug() << "Date is invalid";
        }
        return date.isValid();
    }
}

bool fromStringValue(const QString &inStr, qint32 &value) {
    bool ok = false;
    value = QVariant(inStr).toInt(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, qint64 &value) {
    bool ok = false;
    value = QVariant(inStr).toLongLong(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, bool &value) {
    value = QVariant(inStr).toBool();
    return ((inStr == "true") || (inStr == "false"));
}

bool fromStringValue(const QString &inStr, float &value) {
    bool ok = false;
    value = QVariant(inStr).toFloat(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, double &value) {
    bool ok = false;
    value = QVariant(inStr).toDouble(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, OAIObject &value)
{
    QJsonParseError err;
    QJsonDocument::fromJson(inStr.toUtf8(),&err);
    if ( err.error == QJsonParseError::NoError ){
        value.fromJson(inStr);
        return true;
    }
    return false;
}

bool fromStringValue(const QString &inStr, OAIEnum &value) {
    value.fromJson(inStr);
    return true;
}

bool fromStringValue(const QString &inStr, OAIHttpFileElement &value) {
    return value.fromStringValue(inStr);
}

bool fromJsonValue(QString &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull()) {
        if (jval.isString()) {
            value = jval.toString();
        } else if (jval.isBool()) {
            value = jval.toBool() ? "true" : "false";
        } else if (jval.isDouble()) {
            value = QString::number(jval.toDouble());
        } else {
            ok = false;
        }
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QDateTime &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
            value = QDateTime::fromString(jval.toString(), OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
        } else if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
            value = QDateTime::fromString(jval.toString(), OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
        } else {
            value = QDateTime::fromString(jval.toString(), Qt::ISODate);
        }
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QByteArray &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        value = QByteArray::fromBase64(QByteArray::fromStdString(jval.toString().toStdString()));
        ok = value.size() > 0;
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QDate &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        value = QDate::fromString(jval.toString(), Qt::ISODate);
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(qint32 &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && !jval.isObject() && !jval.isArray()) {
        value = jval.toInt();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(qint64 &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && !jval.isObject() && !jval.isArray()) {
        value = jval.toVariant().toLongLong();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(bool &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isBool()) {
        value = jval.toBool();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(float &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isDouble()) {
        value = static_cast<float>(jval.toDouble());
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(double &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isDouble()) {
        value = jval.toDouble();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(OAIObject &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isObject()) {
        value.fromJsonObject(jval.toObject());
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(OAIEnum &value, const QJsonValue &jval) {
    value.fromJsonValue(jval);
    return true;
}

bool fromJsonValue(OAIHttpFileElement &value, const QJsonValue &jval) {
    return value.fromJsonValue(jval);
}

bool fromJsonValue(QJsonValue &value, const QJsonValue &jval) {
    value = jval;
    return true;
}

} // namespace OpenAPI
