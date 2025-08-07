
import oci


input = """
Você é um especialista técnico em APIs do padrão Open Finance Brasil. Seu objetivo é analisar uma especificação OpenAPI (em JSON) e produzir um relatório detalhado sobre sua conformidade com os padrões oficiais do Open Finance, conforme descrito aqui: https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17377278/Padr+es

A análise deve ser dividida em três seções:
1. Pontos em conformidade com os padrões (exemplos: uso correto de versionamento em `/v1/`, uso de `securitySchemes`, headers padronizados, etc).
2. Pontos fora de conformidade ou ausentes (exemplos: ausência de autenticação OAuth2, estrutura de paths fora do padrão, falta de `info.version`, etc).
3. Sugestões práticas de correção para cada não conformidade detectada (por exemplo: "o path `/cotacoes` deveria seguir o padrão `/v1/market-data/quotes` conforme documento XYZ").

Contexto adicional:
- A análise deve ser técnica e objetiva.
- Use linguagem formal, mas clara.
- Referencie padrões específicos quando possível.
- Considere a estrutura OpenAPI 3.0.

Especificação fornecida:


"""



# Setup basic variables
# Auth Config
# TODO: Please update config profile name and use the compartmentId that has policies grant permissions for using Generative AI Service
compartment_id = "ocid1.tenancy.oc1..aaaaaaaauigv25hxd3re3b2r57j2numpf2wq35ceiyfdqs2ff66evykoy2hq"
CONFIG_PROFILE = "DEFAULT"
config = oci.config.from_file('~/.oci/config', CONFIG_PROFILE)

# Service endpoint
endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"

generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
chat_detail = oci.generative_ai_inference.models.ChatDetails()

content = oci.generative_ai_inference.models.TextContent()
content.text = f"{input}"
message = oci.generative_ai_inference.models.Message()
message.role = "USER"
message.content = [content]

chat_request = oci.generative_ai_inference.models.GenericChatRequest()
chat_request.api_format = oci.generative_ai_inference.models.BaseChatRequest.API_FORMAT_GENERIC
chat_request.messages = [message]
chat_request.temperature = 1


chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyavwbgai5nlntsd5hngaileroifuoec5qxttmydhq7mykq")
chat_detail.chat_request = chat_request
chat_detail.compartment_id = compartment_id

chat_response = generative_ai_inference_client.chat(chat_detail)

# Print result
#print("**************************Chat Result**************************")
if chat_response.data.chat_response.choices[0].message.content[0].text:
    print(chat_response.data.chat_response.choices[0].message.content[0].text)
else:
    print("Resposta não gerada, tente novamente.")


