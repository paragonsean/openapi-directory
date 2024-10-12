/**
 * AIception Interactive
 * Here you can play & test & prototype all the endpoints using just your browser! Go ahead!
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITask.h
 *
 * 
 */

#ifndef OAITask_H
#define OAITask_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITask : public OAIObject {
public:
    OAITask();
    OAITask(QString json);
    ~OAITask() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAnswer() const;
    void setAnswer(const double &answer);
    bool is_answer_Set() const;
    bool is_answer_Valid() const;

    QString getImageUrl() const;
    void setImageUrl(const QString &image_url);
    bool is_image_url_Set() const;
    bool is_image_url_Valid() const;

    QString getThisUrl() const;
    void setThisUrl(const QString &this_url);
    bool is_this_url_Set() const;
    bool is_this_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_answer;
    bool m_answer_isSet;
    bool m_answer_isValid;

    QString m_image_url;
    bool m_image_url_isSet;
    bool m_image_url_isValid;

    QString m_this_url;
    bool m_this_url_isSet;
    bool m_this_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITask)

#endif // OAITask_H
