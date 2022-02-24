import logging
from typing import List, Dict, Any
from paddlenlp.transformers import (UnifiedTransformerLMHeadModel,
                                    UnifiedTransformerTokenizer)

logger = logging.getLogger(__name__)

tokenizer = UnifiedTransformerTokenizer.from_pretrained('plato-mini')
model = UnifiedTransformerLMHeadModel.from_pretrained('plato-mini')

logger.info('Model fully loaded')

def dialog_predict(
    history: List[str],
    **kwargs: Dict[str, Any]
) -> str:
    """
    Predict the next dialog utterance.

    Args:
      history: A list of dialog utterances.
      **kwargs: Additional keyword arguments.

    Returns:
      The predicted dialog utterance.
    """

    inputs = tokenizer.dialogue_encode(
        history,
        add_start_token_as_response=True,
        return_tensors=True,
        is_split_into_words=False
    )

    output_ids, score = model.generate(
        **inputs,
        **kwargs,
    )

    token_ids = output_ids.numpy()[0]

    eos_pos = len(token_ids)
    for i, tok_id in enumerate(token_ids):
        if tok_id == tokenizer.sep_token_id:
            eos_pos = i
            break
    token_ids = token_ids[:eos_pos]
    tokens = tokenizer.convert_ids_to_tokens(token_ids)
    tokens = tokenizer.merge_subword(tokens)

    return ''.join(tokens)

if __name__ == '__main__':
    history = ['你好！']
    print(dialog_predict(history))
