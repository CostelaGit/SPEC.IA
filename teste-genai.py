
import oci


input = """
Olá, bom dia
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
chat_request.max_tokens = 600
chat_request.temperature = 0.7


chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyavwbgai5nlntsd5hngaileroifuoec5qxttmydhq7mykq")
chat_detail.chat_request = chat_request
chat_detail.compartment_id = compartment_id

chat_response = generative_ai_inference_client.chat(chat_detail)

# Print result
print("**************************Chat Result**************************")
print(vars(chat_response))

