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

#ifndef OAI_OBJECT_H
#define OAI_OBJECT_H

#include <QJsonDocument>
#include <QJsonObject>
#include <QMetaType>

namespace OpenAPI {

class OAIObject {
public:
    OAIObject() {}

    OAIObject(QString jsonString) {
        fromJson(jsonString);
    }

    virtual ~OAIObject() {}

    virtual QJsonObject asJsonObject() const {
        return jObj;
    }

    virtual QString asJson() const {
        QJsonDocument doc(jObj);
        return doc.toJson(QJsonDocument::Compact);
    }

    virtual void fromJson(QString jsonString) {
        QJsonDocument doc = QJsonDocument::fromJson(jsonString.toUtf8());
        jObj = doc.object();
    }

    virtual void fromJsonObject(QJsonObject json) {
        jObj = json;
    }

    virtual bool isSet() const {
        return false;
    }

    virtual bool isValid() const {
        return true;
    }

private:
    QJsonObject jObj;
};

inline bool operator==(const OAIObject& left, const OAIObject& right){  
    return (left.asJsonObject() == right.asJsonObject());  
}

inline
#if QT_VERSION < 0x060000
uint
#else
size_t
#endif
qHash(const OAIObject& obj, uint seed = 0) noexcept{
    return qHash(obj.asJsonObject(), seed);
}

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIObject)

#endif // OAI_OBJECT_H
