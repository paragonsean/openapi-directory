/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITextToSpeech.h
 *
 * Request object is used to create a sound from provided text using text to speech engine
 */

#ifndef OAITextToSpeech_H
#define OAITextToSpeech_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITextToSpeech : public OAIObject {
public:
    OAITextToSpeech();
    OAITextToSpeech(QString json);
    ~OAITextToSpeech() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getVoice() const;
    void setVoice(const QString &voice);
    bool is_voice_Set() const;
    bool is_voice_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_voice;
    bool m_voice_isSet;
    bool m_voice_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITextToSpeech)

#endif // OAITextToSpeech_H
